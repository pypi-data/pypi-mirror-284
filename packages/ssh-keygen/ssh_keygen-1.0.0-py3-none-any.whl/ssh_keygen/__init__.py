"""ssh-keygen

# Usage
Generate key from a seed string.
```bash
# Interactive mode (launch a key generation wizard)
python -m ssh_keygen

# Commandline
# -s <seed_string>  The seed string
#                   If not provided, a random string of 128 bits is used.
# -f <file>         Alternatively read the binary data from the file as seed 
# -o <path>         Path to save the private key file
# -n <N=1024>       The number of hash iterations for seed string
#                   Larger N is safer but takes more time.
# -C <comment>      Comment for the generate key
python -m ssh_keygen -s "this is a seed string" -o "/path/to/save/private_key"
python -m ssh_keygen -f "/path/to/seed_file"    -o "/path/to/save/private_key"
```
"""

__version__ = '1.0.0'
