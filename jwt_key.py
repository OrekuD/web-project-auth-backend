

import jwcrypto.jwk as jwk
jwt_key = jwk.JWK.generate(kty='RSA', size=2048)