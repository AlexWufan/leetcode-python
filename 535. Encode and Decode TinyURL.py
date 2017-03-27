class Codec:

    def __init__(self):
        self.url_dic = {}
        self.short_dic = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if not longUrl in self.url_dic:
            self.url_dic[longUrl] = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        if not self.url_dic[longUrl] in self.short_dic:
            self.short_dic[self.url_dic[longUrl]] = longUrl
        return 'http://tinyurl.com/' + self.url_dic[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short_dic[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))