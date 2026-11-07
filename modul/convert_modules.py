import os
import re
import fitz

MODULES = [
    {
        "name": "PBA",
        "input_file": "Modul Petunjuk Praktikum Pemrosesan Bahasa Alami 2026-update_protected.pdf",
        "output_file": "Modul Petunjuk Praktikum Pemrosesan Bahasa Alami 2026-update.md",
        "password": "pba2026",
    },
    {
        "name": "Keamanan Komputer",
        "input_file": "Petunjuk Praktikum keamanan komputer OBE-05092024 - REVISI 14 SEPT 26 V1_protected.pdf",
        "output_file": "Petunjuk Praktikum keamanan komputer OBE-05092024 - REVISI 14 SEPT 26 V1.md",
        "password": "kk2026",
    },
    {
        "name": "Data Mining",
        "input_file": "Rekayasa dan Penambangan Data Petunjuk Praktikum 2026_protected.pdf",
        "output_file": "Rekayasa dan Penambangan Data Petunjuk Praktikum 2026.md",
        "password": "datmin2026",
    },
    {
        "name": "Teknologi Multimedia",
        "input_file": "Rev Petunjuk Praktikum Teknologi Multimedia 2026_protected.pdf",
        "output_file": "Rev Petunjuk Praktikum Teknologi Multimedia 2026.md",
        "password": "tekmul2026",
    },
]

def format_table_to_markdown(table):
    matrix = table.extract()
    if not matrix or not any(any(c for c in row) for row in matrix):
        return ""
    
    cleaned = []
    for row in matrix:
        cleaned_row = []
        for cell in row:
            val = str(cell or "").strip()
            # Fix hyphenated words at line breaks
            val = re.sub(r"(\w+)-\s*\n\s*(\w+)", r"\1\2", val)
            # Replace remaining line breaks with space
            val = re.sub(r"\s*\n\s*", " ", val)
            val = val.replace("|", "\\|")
            cleaned_row.append(val)
        cleaned.append(cleaned_row)
        
    max_cols = max(len(r) for r in cleaned)
    for r in cleaned:
        while len(r) < max_cols:
            r.append("")
            
    header = cleaned[0]
    if all(not c for c in header):
        header = [f"Kolom {i+1}" for i in range(max_cols)]
        body = cleaned
    else:
        body = cleaned[1:] if len(cleaned) > 1 else []
        
    sep = ["---"] * max_cols
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |"
    ]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
        
    return "\n".join(lines)


def is_running_noise(text, y0):
    t = text.strip()
    if not t:
        return True
    # Page number at top or bottom
    if (y0 < 55 or y0 > 790) and re.match(r"^\d+$", t):
        return True
    # Common laboratory header/footer banner
    if "Praktikum" in t and "Informatika" in t and ("UAD" in t or "Universitas Ahmad Dahlan" in t):
        return True
    if re.match(r"^PP/\d+/[A-Z0-9/]+$", t):
        return True
    return False


def process_pdf(pdf_path, password):
    doc = fitz.open(pdf_path)
    if doc.is_encrypted:
        auth = doc.authenticate(password)
        if not auth:
            raise ValueError(f"Password failed for {pdf_path}")
            
    total_pages = len(doc)
    doc_sections = []
    
    for pno in range(total_pages):
        page = doc[pno]
        tabs = page.find_tables()
        tab_bboxes = [fitz.Rect(t.bbox) for t in tabs]
        
        page_items = [] # list of (y0, type, content)
        
        # 1. Extract tables
        for t in tabs:
            tbl_md = format_table_to_markdown(t)
            if tbl_md:
                page_items.append((t.bbox[1], "table", tbl_md))
                
        # 2. Extract text blocks
        page_dict = page.get_text("dict")
        for block in page_dict.get("blocks", []):
            if "lines" not in block:
                continue
                
            b_rect = fitz.Rect(block["bbox"])
            # Skip if inside table area
            if any(b_rect.intersects(tb) for tb in tab_bboxes):
                continue
                
            y0 = block["bbox"][1]
            raw_lines = []
            max_size = 0
            is_bold = False
            total_chars = 0
            mono_chars = 0
            
            for line in block["lines"]:
                line_text = ""
                for span in line["spans"]:
                    st = span["text"]
                    line_text += st
                    font_lower = span["font"].lower()
                    if "courier" in font_lower or "consolas" in font_lower or "mono" in font_lower:
                        mono_chars += len(st.strip())
                    total_chars += len(st.strip())
                    if span["size"] > max_size:
                        max_size = span["size"]
                    if "bold" in font_lower:
                        is_bold = True
                raw_lines.append(line_text)
                
            full_text = "\n".join(raw_lines).strip()
            if not full_text:
                continue
                
            if is_running_noise(full_text, y0):
                continue
                
            is_code = total_chars > 0 and (mono_chars / total_chars) > 0.55
            
            # Formatting determination
            if is_code:
                code_content = "\n".join(raw_lines)
                formatted = f"```\n{code_content}\n```"
                page_items.append((y0, "code", formatted))
            elif max_size >= 16 or re.match(r"^(BAB|MODUL|PERTEMUAN|PRAKTIKUM)\s+\d+", full_text, re.IGNORECASE):
                formatted = f"## {full_text}"
                page_items.append((y0, "h2", formatted))
            elif max_size >= 13 or (is_bold and len(full_text) < 120 and "\n" not in full_text):
                formatted = f"### {full_text}"
                page_items.append((y0, "h3", formatted))
            else:
                # Regular paragraph / list
                # Check if it is a list
                list_match = re.match(r"^([0-9]+\.|\([0-9]+\)|[a-z]\.|\([a-z]\)|[-•*])\s+(.*)", full_text, re.DOTALL)
                if list_match:
                    # Unwrap newlines in list text
                    marker = list_match.group(1)
                    body_text = list_match.group(2)
                    clean_body = " ".join(line.strip() for line in body_text.splitlines() if line.strip())
                    formatted = f"{marker} {clean_body}"
                else:
                    # Normal paragraph: unwrap linebreaks
                    clean_para = " ".join(line.strip() for line in raw_lines if line.strip())
                    formatted = clean_para
                page_items.append((y0, "p", formatted))
                
        page_items.sort(key=lambda x: x[0])
        
        # Merge adjacent code blocks if consecutive
        merged_items = []
        for item in page_items:
            if merged_items and merged_items[-1][1] == "code" and item[1] == "code":
                # combine code blocks
                prev_code = merged_items[-1][2]
                prev_inner = prev_code[4:-4].strip("\n")
                curr_inner = item[2][4:-4].strip("\n")
                combined = f"```\n{prev_inner}\n{curr_inner}\n```"
                merged_items[-1] = (merged_items[-1][0], "code", combined)
            elif merged_items and merged_items[-1][1] == "p" and item[1] == "p":
                # If previous paragraph ended without period or sentence ending, and current starts with lowercase
                prev_text = merged_items[-1][2]
                curr_text = item[2]
                if prev_text and not prev_text.endswith((".", ":", "!", "?", ";")) and curr_text and curr_text[0].islower():
                    combined = prev_text + " " + curr_text
                    merged_items[-1] = (merged_items[-1][0], "p", combined)
                else:
                    merged_items.append(item)
            else:
                merged_items.append(item)
                
        page_body = "\n\n".join(it[2] for it in merged_items)
        if page_body.strip():
            doc_sections.append(f"<!-- Halaman {pno+1} -->\n\n{page_body}")
            
    doc.close()
    return "\n\n---\n\n".join(doc_sections)


def main():
    base_dir = r"c:\Users\firza\Downloads\Laporan\modul"
    print("Mulai proses unlocking dan konversi ke Markdown...")
    
    for mod in MODULES:
        in_path = os.path.join(base_dir, mod["input_file"])
        out_path = os.path.join(base_dir, mod["output_file"])
        
        print(f"\n==========================================")
        print(f"Memproses {mod['name']}:")
        print(f"File input : {mod['input_file']}")
        print(f"File output: {mod['output_file']}")
        
        if not os.path.exists(in_path):
            print(f"ERROR: File {in_path} tidak ditemukan!")
            continue
            
        try:
            md_content = process_pdf(in_path, mod["password"])
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(md_content)
                
            size_kb = os.path.getsize(out_path) / 1024
            print(f"Berhasil! Tersimpan: {mod['output_file']} ({size_kb:.1f} KB)")
        except Exception as e:
            print(f"Gagal memproses {mod['name']}: {e}")
            import traceback
            traceback.print_exc()

    print("\nSemua modul selesai diproses!")

if __name__ == "__main__":
    main()

