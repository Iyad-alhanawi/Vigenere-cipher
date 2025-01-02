<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vigenère Cipher README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>Overview</h1>
    <p>
        This Python program, written from scratch, implements the Vigenère cipher, a classic method for encrypting alphabetic text using polyalphabetic substitution. Users can perform both encryption and decryption using a provided plaintext or ciphertext along with a keyword (cipher key).
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Encryption:</strong> Convert plaintext into ciphertext using a specified key.</li>
        <li><strong>Decryption:</strong> Convert ciphertext back into plaintext using the same key.</li>
        <li><strong>User-Friendly:</strong> Simple command-line interface for easy interaction.</li>
    </ul>

    <h2>Usage</h2>
    <h3>Run the Program:</h3>
    <p>Execute the script in your Python environment.</p>
    
    <h3>Choose Operation:</h3>
    <ul>
        <li>Type <code>encryption</code> to encrypt text.</li>
        <li>Type <code>decryption</code> to decrypt text.</li>
    </ul>

    <h3>Input:</h3>
    <ul>
        <li>For encryption: Enter the plaintext and a key (lowercase letters only).</li>
        <li>For decryption: Enter the ciphertext and the same key used for encryption.</li>
    </ul>

    <h3>Output:</h3>
    <p>The program will display the encrypted or decrypted text.</p>

</body>
</html>
