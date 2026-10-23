js_code = """
console.log("Hola desde un archivo js generado con python")

function suma(a,b) {
    return a + b;
}
"""

with open("script.js", "w") as filejs:
    filejs.write(js_code)