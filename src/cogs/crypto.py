import zlib, gzip, hashlib, secrets, string

from uuid import uuid4
from selfcord.ext import commands
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from src.utils import *

class Crypto(commands.Cog):
    """
    Everything cryptography. Encryption, compression, passwords and more
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(aliases=['get-entropy'])
    async def entropy(self, ctx, *, msg) -> None:
        """
        Computes the entropy of the given message
        """

        """
        await entropy(context, message) -> nothing

        Computes the entropy of the given message

        :param ctx object: Context
        :param msg str: Message/data to compute entropy of
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        entropy = await get_entropy(msg)

        await sendmsg(
            ctx,
            (
                f'**Data**: `{msg}`\n'
                f'**Entropy**: `{entropy}`'
            )
        )

    @commands.command(aliases=['seedgen'])
    async def seed(self, ctx, length: int = 24) -> None:
        """
        Generates a secure random seed
        """

        """
        await seed(context, length) -> nothing

        Generates a secure random seed

        :param ctx object: Context
        :param length int: Length
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        seed = ' '.join(secrets.choice(dictionary) for _ in range(length))
        entropy = await get_entropy(seed)
        
        await sendmsg(
            ctx,
            (
                f'**Seed**: `{seed}`\n'
                f'**Entropy**: `{entropy}`'
            ),
            False
        )
    
    @commands.command(aliases=['passwordgen', 'pwgen'])
    async def password(self, ctx, length=24) -> None:
        """
        Securely generates a password
        """

        """
        await password(context, length) -> nothing

        Securely generates a password

        :param ctx object: Context
        :param length int: Length
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        password = ''.join([
            secrets.choice(
                string.ascii_lowercase
                +string.ascii_uppercase
                +string.digits
            ) for _ in range(length)
        ])

        entropy = await get_entropy(password)
        
        await sendmsg(
            ctx,
            (
                f'**Password**: ||{password}||\n'
                f'**Entropy**: `{entropy}`'
            ),
            False
        )
    
    @commands.command(aliases=['b64enc', 'b64encode', 'base64enc', 'base64encode'])
    async def b64_enc(self, ctx, *, msg) -> None:
        """
        Base 64 encodes the given message, and sends it
        """

        """
        await b64_enc(context, message) -> nothing

        Base 64 encodes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to encode and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx, 
            b64encode(msg.encode()).decode(),
            False
        )
    
    @commands.command(aliases=['b64dec', 'b64decode', 'base64dec', 'base64decode'])
    async def b64_dec(self, ctx, *, msg) -> None:
        """
        Base 64 decodes the given message, and sends it
        """

        """
        await b64_dec(context, message) -> nothing

        Base 64 decodes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to decode and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx, 
            b64decode(msg.encode()).decode(), 
            False
        )
    
    @commands.command(aliases=['zlibcomp', 'zlibcompress', 'zlib-compress'])
    async def zlib_compress(self, ctx, *, msg) -> None:
        """
        Compresses the given message, and sends it
        """

        """
        await zlib_compress(context, message) -> nothing

        Compresses the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to compress and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            zlib.compress(msg.encode(), 9).hex(),
            False
        )
    
    @commands.command(aliases=['zlibdecomp', 'zlibdecompress', 'zlib-decompress'])
    async def zlib_decompress(self, ctx, *, msg) -> None:
        """
        Decompresses the given message, and sends it
        """

        """
        await zlib_decompress(context, message) -> nothing

        Decompresses the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to decompress and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            zlib.decompress(msg.encode().from_hex(msg)).decode(),
            False
        )

    @commands.command(aliases=['gzipcomp', 'gzipcompress', 'gzip-compress'])
    async def gzip_compress(self, ctx, *, msg) -> None:
        """
        Compresses the given message, and sends it
        """

        """
        await gzip_compress(context, message) -> nothing

        Compresses the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to compress and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            gzip.compress(msg.encode(), 9).hex(),
            False
        )
    
    @commands.command(aliases=['gzipdecomp', 'gzipdecompress', 'gzip-decompress'])
    async def gzip_decompress(self, ctx, *, msg) -> None:
        """
        Decompresses the given message, and sends it
        """

        """
        await gzip_decompress(context, message) -> nothing

        Decompresses the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to decompress and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            gzip.decompress(msg.encode().from_hex(msg)).decode(),
            False
        )
    
    @commands.command(aliases=['md5', 'md5hash'])
    async def md5_hash(self, ctx, *, msg) -> None:
        """
        Hashes the given message, and sends it
        """

        """
        await md5_hash(context, message) -> nothing

        Hashes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to hash and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            hashlib.md5(msg.encode()).hexdigest(),
            False
        )
    
    @commands.command(aliases=['sha224', 'sha224hash'])
    async def sha224_hash(self, ctx, *, msg) -> None:
        """
        Hashes the given message, and sends it
        """

        """
        await sha224_hash(context, message) -> nothing

        Hashes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to hash and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            hashlib.sha224(msg.encode()).hexdigest(),
            False
        )
    
    @commands.command(aliases=['sha256', 'sha256hash'])
    async def sha256_hash(self, ctx, *, msg) -> None:
        """
        Hashes the given message, and sends it
        """

        """
        await sha256_hash(context, message) -> nothing

        Hashes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to hash and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            hashlib.sha256(msg.encode()).hexdigest(),
            False
        )
    
    @commands.command(aliases=['sha512', 'sha512hash'])
    async def sha512_hash(self, ctx, *, msg) -> None:
        """
        Hashes the given message, and sends it
        """

        """
        await sha512_hash(context, message) -> nothing

        Hashes the given message, and sends it

        :param ctx object: Context
        :param msg str: Message to hash and send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            hashlib.sha512(msg.encode()).hexdigest(),
            False
        )
    
    @commands.command(aliases=['uuid', 'uuid4', 'makeuuid'])
    async def make_uuid(self, ctx) -> None:
        """
        Generates a random UUID
        """

        """
        await make_uuid(context) -> nothing

        Generates a random UUID using the UUID library

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            str(uuid4.uuid()),
            False
        )
    
    @commands.command(aliases=['aescrypt', 'aesencrypt', 'aes-encrypt'])
    async def aes_encrypt(self, ctx, key, nonce, *, msg) -> None:
        """
        AES Encrypts your message
        """

        """
        await aes_encrypt(context, message) -> nothing

        AES Encrypts the given message, with the key and nonce

        :param ctx object: Context
        :param msg str: Data to encrypt
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if len(key) != 32:
            await sendmsg(ctx, '**Error**: `Key must be be 32 characters`')
        
        elif len(nonce) != 16:
            await sendmsg(ctx, '**Error**: `Nonce must be 16 characters`')
        
        else:
            cipher = Cipher(algorithms.AES(key.encode()), modes.OFB(nonce.encode()))
            encryptor = cipher.encryptor()

            ct = encryptor.update(msg.encode()) + encryptor.finalize()

            await sendmsg(
                ctx,
                ct.hex(),
                False
            )
    
    @commands.command(aliases=['aesdecrypt', 'aes-decrypt'])
    async def aes_decrypt(self, ctx, key, nonce, *, msg) -> None:
        """
        AES Decrypts your message
        """

        """
        await aes_decrypt(context, message) -> nothing

        AES decrypts the given ciphercode using the key and nonce

        :param ctx object: Context
        :param msg str: Data to decrypt
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if len(key) != 32:
            await sendmsg(ctx, '**Error**: `Key must be be 32 characters`')
        
        elif len(nonce) != 16:
            await sendmsg(ctx, '**Error**: `Nonce must be 16 characters`')
        
        else:
            cipher = Cipher(algorithms.AES(key.encode()), modes.OFB(nonce.encode()))
            decryptor = cipher.decryptor()

            cleartext = decryptor.update(msg.encode().fromhex(msg)) + decryptor.finalize()

            await sendmsg(
                ctx,
                cleartext.decode(),
                False
            )

async def setup(client):
    await client.add_cog(Crypto(client))