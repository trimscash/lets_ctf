from Crypto.Util.number import *

p = 10118035214116383481316889347194724393608343649131542259967893120533595570110964519235816949215472081912451708786559633812826294399002530904413303670406779
q = 11913493220565146468618714749925727243648727543641169365479499790994492274460827985035062541001885391058329154734729111384057356210581540680556707443254101
e = 65537
c = 73259438438885065619821575258541239860603937294624240652270783150642855640732960474164051774190494630031331834866754333306317422750451230460849221418756193466721533423819722686539554830189892056893472780030576639586036544040636421625652245274163633679561624594821479781511324837136855647075931627208059359269
n = p*q

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

dec = pow(c, d, n)

print(long_to_bytes(dec))
