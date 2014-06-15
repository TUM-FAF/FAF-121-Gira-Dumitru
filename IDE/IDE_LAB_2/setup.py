from cx_Freeze import setup, Executable

setup(
    name = "Simulatron",
    version = "1.0.0",
    description = "Laboratory Work Nr.2 on IDE",
    executables = [Executable("main.py")])