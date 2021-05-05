import json

spec_json='riscv-isa-properties.json'
modules_rv32 = {}
modules_rv64 = {}
formats = {}

def parse_modules():
    f = open (spec_json, "r")
    data = json.loads(f.read())

    # show_modules = ["I", "I priviledged", "A", "M", "F", "D", "C"]
    show_modules = ["I", "I priviledged", "A", "M", "F", "D", "C", "FC", "DC"]
    for module in data['modules']:
        if module in show_modules:
            for arch in data['modules'][module]:

                if arch == "RV32":
                    modules_rv32[module] = data['modules'][module][arch]

                if arch == "RV64":
                    modules_rv64[module] = data['modules'][module][arch]
    f.close()

def parse_formats():
    f = open (spec_json, "r")
    data = json.loads(f.read())
    for each in data['formats']:
        # print(data['formats'][each])
        formats[each] = data['formats'][each]
    f.close()

def instruction_index_one_arch(file, dictionary, arch_name):
    file.write("\n")
    file.write("## " + arch_name + "\n")
    for module in dictionary:
        file.write("\n")
        file.write("### " + arch_name + module + "\n")
        for instruction in dictionary[module]:
            file.write(" - " + instruction + "\n")

def generate_index_modules():
    f = open("instructions_generated/index.md", "w")
    f.write("# Modules\n")
    instruction_index_one_arch(f, modules_rv32, "RV32")
    instruction_index_one_arch(f, modules_rv64, "RV64")
    f.close()


def generate_index_formats():
    f = open("instructions_generated/index.md", "a")
    f.write("# Formats\n\n")
    for entry in formats:
        # print(entry)
        f.write("## " + entry + " - " + formats[entry]['meaning'] + "\n")

        f.write("\n")
        f.write("```{wavedrom}\n")
        f.write("---\n")
        f.write("height: 300px\n")
        f.write("width: 840 px\n")
        f.write("---\n")
        f.write("{\"reg\": [\n")

        first = True

        for register in formats[entry]['format']:
            bits = formats[entry]['format'][register]
            if first:
                first = False
            else:
                f.write(",")

            types = {
                "rd": 2,
                "rd'": 2,
                "rs1": 3,
                "rs1'": 3,
                "rs2": 4,
                "rs2'": 4,
                "rd/rs1": 5,
                "rd'/rs1'": 5
            }

            registerType = 0
            if register in types:
                registerType = types[register]

            f.write("{\"bits\": " + str(bits) + ", \"name\": \"" + register + "\"");
            if registerType > 0:
                f.write(", \"type\": " + str(registerType))
            f.write("}\n")

        f.write("]\n")

        if entry.startswith("C"):
            f.write(", \"config\":{\"bits\": 16} \n")

        f.write("}\n")
        f.write("```\n")
        f.write("\n\n")
    f.close()

parse_formats()
parse_modules()

generate_index_modules()
generate_index_formats()


