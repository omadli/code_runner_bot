from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DEBUG = env.bool("DEBUG")
ADMINS = env.list("ADMINS")
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
    
    "php": {
        "name": "php",
        "command": "php",
        "file_name": "test.php",
        "version": "8.2.3",
        "example": "<?php\n    echo \"Hello world\"\n?>"
    },
    
    "python": {
        "name": "python",
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
}
