# Batch File Encryptor

This Python program applies a simple byte modification to "encrypt" a batch file, rendering its source code unreadable. The program prepends a custom byte sequence to the file, making it appear garbled when opened in a standard text editor.

## How It Works

The encryptor adds the following byte sequence to the beginning of the batch file:
```FF FE 26 63 6C 73 0D 0A```. This causes the file to display unintelligible characters instead of its actual content.


## Example

### Before Encryption:
```
@echo off
echo hello world
pause
exit
```

### After Encryption:
```
挦獬਍敀档⁯景൦攊档⁯敨汬⁯潷汲൤瀊畡敳਍硥瑩
```
Although the batch file will still execute normally, its contents will be obscured when viewed in a text editor.

## Usage

1. Download the program
2. Run the program:
```python batch-encryptor.py```

> [!WARNING]
> This encryption method is not secure! If someone uses a hex editor, they can easily remove the added byte sequence and reveal the original batch file contents. Use this program only for basic obfuscation, not for sensitive data protection.

You can join my [Discord](https://discord.gg/N55YYbDZ7Z) for more tools and informations!
