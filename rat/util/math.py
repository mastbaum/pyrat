'''Extra math functions.'''

def radical_inverse(n, base):
    '''from RAT::RadicalInverse.'''
    val = 0.0
    inv_base = 1.0/base
    inv_bi = inv_base

    while n > 0:
        d_i = (n % base)
        val += d_i * inv_bi
        n /= base
        inv_bi *= inv_base

    return val

