from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DEBUG = env.bool("DEBUG")
ADMINS = list(map(int, env.list("ADMINS")))
DB_URL = env.str("DB_URL")
USE_REDIS = env.bool("USE_REDIS", False)
REDIS_DB = env.int("REDIS_DB", 0)
REDIS_PASSWORD = env.str("REDIS_PASSWORD", None)


TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

LANGUAGES = {
    "c": {
        "name": "c",
        "command": "c",
        "file_name": "test",
        "version": "10.2.0",
        "example": "#include <stdio.h>\nint main(){\n\tprintf(\"Hello world\");\n\treturn 0;\n}"
    },
    
    "cpp": {
        "name": "c++",
        "command": "cpp",
        "file_name": "test",
        "version": "10.2.0",
        "example": "#include <iostream>\n"
                    "using namespace std;\n"
                    "int main(){\n"
                    "    cout << \"Hello world\" << endl;\n"
                    "    return 0;\n"
                    "}"
    },
    
    "csharp": {
        "name": "c#",
        "command": "csharp",
        "file_name": "test.cs",
        "version": "5.0.201",
        "example": "// Hello World! program\nnamespace HelloWorld\n{\n    class Hello {         "
                    "\n        static void Main(string[] args)\n        {\n            "
                    "System.Console.WriteLine(\"Hello World!\");\n        }\n    }\n}"
    },
    
    "java": {
        "name": "java",
        "command": "java",
        "file_name": "test",
        "version": "15.0.2",
        "example": "class HelloWorld {\n"
                    "\tpublic static void main(String[] args) {\n"
                    "\t\tSystem.out.println(\"Hello, World!\"); \n\t}\n}"
    },
    
    "kotlin": {
        "name": "kotlin",
        "command": "kotlin",
        "file_name": "test",
        "version": "1.8.20",
        "example": "fun main(args : Array<String>) {\n\tprintln(\"Hello, World!\")\n}"
    },
    
    "javascript": {
        "name": "javascript",
        "command": "js",
        "file_name": "test.js",
        "version": "18.15.0",
        "example": "console.log(\"Hello world\")"
    },
    
    "typescript": {
        "name": "typescript",
        "command": "ts",
        "file_name": "test.ts",
        "version": "1.32.3",
        "example": "let message: string = 'Hello, World!';\nconsole.log(message);"
    },
    
    "php": {
        "name": "php",
        "command": "php",
        "file_name": "test.php",
        "version": "8.2.3",
        "example": "<?php\n    echo \"Hello world\"\n?>"
    },
    
    "python2": {
        "name": "python2",
        "command": "python2",
        "file_name": "test.py",
        "version": "2.7.18",
        "example": "print \"Hello world\""
    },
    
    "python": {
        "name": "python3",
        "command": "python",
        "file_name": "test.py",
        "version": "3.10.0",
        "example": "print(\"Hello world\")"
    },
    
    "go": {
        "name": "go",
        "command": "go",
        "file_name": "test",
        "version": "1.16.2",
        "example": "package main\n\nimport \"fmt\"\nfunc main() {\n\tfmt.Println(\"hello world\")\n}"
    },
    
    "rust": {
        "name": "rust",
        "command": "rust",
        "file_name": "test.rs",
        "version": "1.68.2",
        "example": "fn main() {\n\tprintln!(\"Hello World!\");\n}"
    },
    
    "dart": {
        "name": "dart",
        "command": "dart",
        "file_name": "test.dart",
        "version": "2.19.6",
        "example": "void main() {\n  print(\"Hello, World!\");\n}"
    },
    
    "emojicode": {
        "name": "emojicode",
        "command": "emojicode",
        "file_name": "test.emojic",
        "version": "1.0.2",
        "example": "🏁 🍇\n  😀 🔤Hello World!🔤❗️\n🍉"
    },
    
    "haskell": {
        "name": "haskell",
        "command": "haskell",
        "file_name": "test",
        "version": "9.0.1",
        "example": "main = do\n  putStrLn \"Hello, everybody!\""
    },
    
    "pascal": {
        "name": "pascal",
        "command": "pascal",
        "file_name": "test.pas",
        "version": "3.2.2",
        "example": "program Hello;\nbegin\n  writeln ('Hello, world.');\nend."
    },
    
    "ruby": {
        "name": "ruby",
        "command": "ruby",
        "file_name": "test.rb",
        "version": "3.0.1",
        "example": "puts \"Hello wordl\""
    },
    
    "swift": {
        "name": "swift",
        "command": "swift",
        "file_name": "test.swift",
        "version": "5.3.3",
        "example": "print(\"Hello, World!\")"
    },
    
    "sql": {
        "name": "sqlite3",
        "command": "sql",
        "file_name": "test.sql",
        "version": "3.36.0",
        "example": "SELECT \"Hello world\";"
    },
    
    "nasm": {
        "name": "nasm64",
        "command": "nasm",
        "file_name": "test.asm",
        "version": "2.15.5",
        "example": '          global    _start\n\n'
                   '          section   .text\n'
                   '_start:   mov       rax, 1\n'
                   '          mov       rdi, 1\n'
                   '          mov       rsi, message\n'
                   '          mov       rdx, 13\n'
                   '          syscall \n'
                   '          mov       rax, 60 \n'
                   '          xor       rdi, rdi \n'
                   '          syscall \n\n'
                   '          section   .data\n'
                   'message:  db        "Hello, World", 10 '
    },
    
}
