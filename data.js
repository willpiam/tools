const tools = [
    {
        title: "Encoding Converter",
        description: "Convert between text, hex, base64, and base64Url formats",
        path: "encodingConverter.html"
    },
    {
        title: "Kiss My AES",
        description: "A simple tool to encrypt and decrypt messages using AES. K.I.S.S - Keep It Simple Stupid",
        path: "kiss_my_AES.html"
    },
    {
        title: "Simple OTP Encryption",
        description: "A simple tool for one time pad (OTP) encryption/decryption and key generation",
        path: "otp.html"
    },
    {
        title: "Password Generator",
        description: "Generate secure passwords with customizable options",
        path: "passwordmaker.html"
    },
    {
        title: "QR Code Generator",
        description: "Create a QR code given a string",
        path: "qrcodeMaker.html"
    },
    {
        title: "ECC Asymmetric Encryption Tool",
        description: "Encrypt and decrypt messages using ECC asymmetric encryption",
        path: "asymmetric.html"
    },
    {
        title: "Hex Differ",
        description: "Compare multiple hex strings and highlight their differences",
        path: "hexCompare.html"
    },
    {
        title: "Dice Roller",
        description: "Roll dice and see the results",
        path: "dice.html"
    },
    {
        title: "HTML Renderer",
        description: "Paste HTML and view it rendered in a sandboxed preview",
        path: "htmlRenderer.html"
    },
    {
        title: "JWT Decoder",
        description: "Decode JSON Web Tokens to inspect the header, payload, and claims",
        path: "jwtDecoder.html"
    },
    {
        title: "Emoji Picker",
        description: "Search Unicode emoji by name and copy them with one tap",
        path: "emojiPicker.html"
    },
    {
        title: "SHA-256 Lowest Hash Miner",
        description: "Mine for the lowest SHA-256 hash using input + nonce with pause and JSON import/export",
        path: "sha256Miner.html"
    },
    {
        title: "File SHA-256 Hasher",
        description: "Upload a file, compute its SHA-256 hash, and copy the result",
        path: "fileSha256.html"
    },
    {
        title: "Written In Stone: An On-Chain Messaging and Commitment Tool",
        description: `Write arbitrary data to the blockchain with a flexible commitment toolkit. You can commit plain text directly, hash text before committing, or hash files and commit the resulting digest. Encrypted text commitments are also supported using AES. The tool works on both Ethereum and Cardano, using Input Data Messages on Ethereum and CIP-20 on Cardano. On Cardano, you can also use an NFT to link multiple commitments into a verifiable chain.`,
        mode: "external", // indicates that this tool is hosted elsewhere... a url field is provided in place of a path field
        url: "https://cardano-tools-delta.vercel.app/commit"
    }
];
