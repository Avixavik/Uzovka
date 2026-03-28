import tempfile
import sys
import užovka_lib as u

def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        print("(x): CFx404: File not found.")
        sys.exit(4404)

    with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp:
        import re
        replacements = [
            (r"\binak\b", "else"),
            (r"\balebo\b", "elif"),
            (r"\bak\b", "if"),
            (r"\bpre\b", "for"),
            (r"\bkým\b", "while"),
            (r"\bvrátiť\b", "return"),
            (r"\bzhoda\b", "match"),
            (r"\bprípad\b", "case"),
            (r"\bprerušiť\b", "break"),
            (r"\bpokračovať\b", "continue"),
            (r"\bskúsiť\b", "try"),
            (r"\bokrem\b", "except"),
            (r"\bnakoniec\b", "finally"),
            (r"\btrieda\b", "class"),
            (r"\bimportovať\b", "import"),
            (r"\bz\b", "from"),
            (r"\bako\b", "as"),
            (r"\bz\b", "with"),
            (r"\bvytlačiť\b", "print"),
            (r"\bimportovať\b", "import"),
            (r"\bvšetko\b", "all"),
            (r"\bniečo\b", "any"),
            (r"\baďaľší\b", "anext"),
            (r"\blogický\b", "bool"),
            (r"\bbodprerušenia\b", "breakpoint"),
            (r"\bpolebajtov\b", "bytearray"),
            (r"\bbajty\b", "bytes"),
            (r"\bvolateľný\b", "callable"),
            (r"\bznak\b", "chr"),
            (r"\bmetódatriedy\b", "classmethod"),
            (r"\bskompilovať\b", "compile"),
            (r"\bkomplexnéčíslo\b", "complex"),
            (r"\bvymazaťatr\b", "delattr"),
            (r"\bslovník\b", "dict"),
            (r"\bzoznamatr\b", "dir"),
            (r"\bpodielzvyšok\b", "divmod"),
            (r"\bočíslovať\b", "enumerate"),
            (r"\bvyhodnotiť\b", "eval"),
            (r"\bspustiť\b", "exec"),
            (r"\bfiltrovať\b", "filter"),
            (r"\bdesatinné\b", "float"),
            (r"\bformátovať\b", "format"),
            (r"\bzmrazenámnožina\b", "frozenset"),
            (r"\bzískaťatr\b", "getattr"),
            (r"\bglobálne\b", "globals"),
            (r"\bmáatr\b", "hasattr"),
            (r"\bhaš\b", "hash"),
            (r"\bpomoc\b", "help"),
            (r"\bšestnástkovo\b", "hex"),
            (r"\bvstup\b", "input"),
            (r"\bceléčíslo\b", "int"),
            (r"\bjeinštanciov\b", "isinstance"),
            (r"\bjepodtriedov\b", "issubclass"),
            (r"\biterátor\b", "iter"),
            (r"\bdĺžka\b", "len"),
            (r"\bzoznam\b", "list"),
            (r"\blokálne\b", "locals"),
            (r"\bmapovať\b", "map"),
            (r"\bpohladdopamäte\b", "memoryview"),
            (r"\bďalší\b", "next"),
            (r"\botvoriť\b", "open"),
            (r"\bordinálnahodnota\b", "ord"),
            (r"\bosmičkovo\b", "oct"),
            (r"\bobjekt\b", "object"),
            (r"\bmocnina\b", "pow"),
            (r"\bvlastnosť\b", "property"),
            (r"\brozsah\b", "range"),
            (r"\breprezentácia\b", "repr"),
            (r"\bobrátené\b", "reversed"),
            (r"\bzaokrúhliť\b", "round"),
            (r"\bmnožina\b", "set"),
            (r"\bnastaviťatr\b", "setattr"),
            (r"\brez\b", "slice"),
            (r"\broztriedené\b", "sorted"),
            (r"\bstatickámetóda\b", "staticmethod"),
            (r"\breťazec\b", "str"),
            (r"\bsúčet\b", "sum"),
            (r"\bnadradený\b", "super"),
            (r"\bn-tica\b", "tuple"),
            (r"\btyp\b", "type"),
            (r"\bpremenné\b", "vars"),
            (r"\bzips\b", "zip"),
            (r"\b__importovať__\b", "__import__"),
        ]

        def translate_outside_quotes(text):
            parts = re.split(r'(".*?"|\'.*?\')', text, flags=re.DOTALL)
            for i, part in enumerate(parts):
                if len(part) > 0 and part[0] in "\"'":
                    continue
                for pattern, repl in replacements:
                    part = re.sub(pattern, repl, part)
                parts[i] = part
            return "".join(parts)

        edited_content = translate_outside_quotes(content)

        temp.write(edited_content)
        temp.flush()
        temp.seek(0)
        exec(temp.read())


main()