import sympy as sp

x = sp.symbols('x')

def lagrange_poly(data,interpolate):
    lagrange_list = []
    lagrange_product = {}
    
    for pair in data:
        for x_value in data:
            if pair != x_value:
                lagrange_list.append(
                    (x - x_value[0])/(pair[0] - x_value[0]))
                
    product_index = 0
    lagrange_product[0] = lagrange_list[0]
    
    for values in range(1, len(lagrange_list)):
        if  values % (len(data)-1) == 0:
            product_index += 1
            lagrange_product[product_index] = lagrange_list[values]
        else:
            lagrange_product[product_index] = (
                lagrange_product[product_index] * lagrange_list[values])
            
    for term in range(len(lagrange_product)):
        lagrange_product[term] = lagrange_product[term] * data[term][1]
    final_poly = (sum(lagrange_product.values()))

    print("P(x) =", final_poly)
    return final_poly.subs(x,interpolate)

data1 = [[-1, 0.861], [-.5, 0.958], [0, 1.09], [.5, 1.29]]
data2 = [[2,5],[5,8],[8,9],[11,44],[12,8],[14,7],[15,8],[16,14],[20,66]]

# Interpolate on (data set, point)
#lagrange_poly(data1,.25)
lagrange_poly(data2,19)
