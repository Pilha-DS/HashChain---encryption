# HashChain---encryption V1.0.0
   A simple encryption system that uses combinations of # and * to securely represent text, with integrated compression and multiple layers of security.

   ✨ Main Features
   🔒 Strong Encryption: Algorithm based on numeric seeds and substitution tables

   🗜️ Integrated Compression: Specialized compression system for # and * sequences

   🔑 Key Management: Unified system for easy decryption

   🛡️ Analysis-Resistant: No identifiable visual patterns

   🚀 How to Use

   git clone https://github.com/Pilha-DS/HashChain---encryption


   Encrypt text.

   python

   #Encryption  

   #Decryption  

   #Compression  

   #Decompression  


   📦 Project Structure

   HashChain---encryption/ 
   └── funcional/
      ├── HashChainApp.py     # Encryption application
      ├── HashChainApp.py     # Encryption terminal
      ├── compressor.py       # Simple compression
      ├── descompressor.py    # Simple decompression
      ├── tables.py           # Table generation
      ├── grafador.py         # Key management
      └── desgrafar.py        # Key management


   🛡️ Security Levels
   🔐 Basic Encryption

   #8-digit seed, default table range
   result = grafar("text", seed=12345678)


   📊 Performance

   Operation	Avg. Time	Compression Rate	Security
   Encryption	15ms	-	🔒🔒🔒🔒
   Decryption	12ms	-	🔒🔒🔒🔒
   Compression	8ms	35-85%	-
   Decompression	5ms	-	-

   🚨 Known Limitations
   ❌ Reduced efficiency with very short texts (<10 characters)
   ❌ Overhead in highly alternating sequences (###*)
   ❌ Need for secure seed management

   🚧 Planned Features

   Web-based graphical interface

   REST API for integration

   Browser plugins

   iOS/Android mobile app

   📝 License
   This project is under the MIT license. See the LICENSE file for details.

   🆘 Support
   Found a problem? Open an issue or contact:
   📧 Email: jsc.sanchescardoso@gmail.com

   ⭐ Acknowledgments
   Encryption algorithm developed with a focus on security and efficiency.
   Version 1 was created as a college project, designed to be as simple as possible.

   Optimized compression system for symbol patterns
   Intuitive interface for end users