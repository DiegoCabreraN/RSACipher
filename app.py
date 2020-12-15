import sys
from RSA import RSA

cryptography = RSA()

if len(sys.argv) > 1:
    if '--encrypt' in sys.argv[1]:
        original = sys.argv[1].split('=')[1]
        encoded = cryptography.encodeString(original)
        print('\n{} encoded to {}\n'.format(original, encoded))

    elif '--decrypt' in sys.argv[1]:
        encrypted = sys.argv[1].split('=')[1]
        decoded = cryptography.decodeString(encrypted)
        print('\n{} decoded to {}\n'.format(encrypted, decoded))

    else:
        print('\nError with method, try again.')
        print('Usage:\n\tpython app.py --encrypt="<original>"')
        print('\tpython app.py --decrypt="<encrypted>"\n')
else:
    print('\nError with method, try again.')
    print('\nUsage:\n\tpython app.py --encrypt="<original>"')
    print('\tpython app.py --decrypt="<encrypted>"\n')