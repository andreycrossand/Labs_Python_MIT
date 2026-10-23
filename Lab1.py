# polynomial.py

class Polynomial:

    def __init__(self, *coefficients):
        self.coeffs = {}
        if len(coefficients) > 1:
            self.coeffs = dict(enumerate(coefficients))
        elif len(coefficients) == 1:
            arg = coefficients[0]
            if isinstance(arg, (list,tuple)):
                self.coeffs = dict(enumerate(arg))
            elif isinstance(arg, dict):
                self.coeffs = arg.copy()
            elif isinstance(arg, Polynomial):
                self.coeffs = arg.coeffs.copy()
            elif isinstance(arg, (int, float)):
                self.coeffs = {0: arg}
        clean = {key: value for key, value in self.coeffs.items() if value != 0}
        self.coeffs = dict(sorted(clean.items(), key = lambda item: item[0], reverse = True))

    def __repr__(self):
        if not self.coeffs:
            return "Polynomial [0]"

        max_deg = next(iter(self.coeffs))
        coeffs_list = [self.coeffs.get(i, 0) for i in range(max_deg + 1)]

        return f"Polynomial {coeffs_list}"

    def __str__(self):
        if not self.coeffs:
            return "0"
        result = []
        is_first = True
        for key, value in self.coeffs.items():
            if key == 0:
                x_part = ""
            elif key == 1:
                x_part = "x"
            else:
                x_part = f"x^{key}"

            if abs(value) == 1 and key != 0:
                num_part = ""
            else:
                num_part = str(abs(value))

            if is_first:
                sign = "" if value > 0 else "-"
                is_first = False
            else:
                sign = " + " if value > 0 else " - "

            result.append(f"{sign}{num_part}{x_part}")
        return "".join(result)

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            try:
                other = Polynomial(other)
            except Exception:
                return False
        return self.coeffs == other.coeffs

    def __add__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        res_coeffs = self.coeffs.copy()
        for key, value in other.coeffs.items():
            res_coeffs[key] = res_coeffs.get(key, 0) + value
        return Polynomial(res_coeffs)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        neg_coeffs = {key: -value for key, value in self.coeffs.items()}
        return Polynomial(neg_coeffs)

    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        res_coeffs = self.coeffs.copy()
        for key, value in other.coeffs.items():
            res_coeffs[key] = res_coeffs.get(key, 0) - value
        return Polynomial(res_coeffs)

    def __rsub__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        return other - self

    def __call__(self, x):
        result = 0
        for key, value in self.coeffs.items():
            result += (value * (x ** key))
        return result

    def degree(self):
        if not self.coeffs:
            return 0
        else:
            return max(self.coeffs.keys())

    def der(self, d=1):
        dif_poly = self.coeffs.copy()
        for i in range(d):
            new_coeffs = {}
            for key, value in dif_poly.items():
                if key > 0:
                    new_coeffs[key - 1] = value * key
            dif_poly = new_coeffs
        return Polynomial(dif_poly)

    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial(other)
        new_coeffs = {}
        for key1, value1 in self.coeffs.items():
            for key2, value2 in other.coeffs.items():
                new_key = key1 + key2
                new_value = value1 * value2

                new_coeffs[new_key] = new_coeffs.get(new_key, 0) + new_value

        return Polynomial(new_coeffs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        self.pairs = iter(list(self.coeffs.items()))
        return self

    def __next__(self):
        return(next(self.pairs))

