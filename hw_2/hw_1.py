import math

i_1 = 8
i_2 = 2
result_sum = i_1 + i_2

print('result_sum =',result_sum)

number = (i_1,i_2)
result_subtr = min(number) - max(number)
print('result_subtr =',result_subtr)

result_multi = i_1 * i_2
print('result_multi =',result_multi)

result_exp = i_1 ** i_2
print('result_exp =',result_exp)

result_m_exp = math.pow(i_1,i_2)
print('result_m_exp =',result_m_exp)

result_s_root = i_1 ** 0.5
print('result_s_root =',result_s_root)

result_m_s_root = math.sqrt(i_1)
print('result_m_s_root =',result_m_s_root)

result_mp_s_root = math.pow(i_1, 0.5)
print('result_mp_s_root =',result_mp_s_root )

i_1 = 7
i_2 = 4
result_division = i_1 / i_2
print('result_devision =',result_division)

result_m_floor = math.floor(result_division)
print('result_m_floor =',result_m_floor)

result_m_ceil= math.ceil(result_division)
print('result_m_ceil =',result_m_ceil)

result_int = round(result_division)
print('result_int =',result_int)

result_no_division_loss = i_1 // i_2
print('result_no_division_loss =',result_no_division_loss)

result_division_loss = i_1 % i_2
print('result_division_loss =',result_division_loss)

i_3 = 5

i_3 += 10
print('i_3 =',i_3)
i_3 -= 5
print('i_3 =',i_3)
i_3 *= 3
print('i_3 =',i_3)
i_3 /= 2
print('i_3 =',i_3)
i_3 **= 2
print('i_3 =',i_3)
i_3 **= 0.5
print('i_3 =',i_3)
i_3 %= 2
print('i_3 =',i_3)

#Boolean (True=1;False=0)

b_item_t = True
b_item_f = False

b_item_result_sum = b_item_t + b_item_f
print('b_item_result_sum =', b_item_result_sum)

b_item_result_subtr = b_item_t - b_item_f
print('b_item_result_subtr =',b_item_result_subtr)

b_item_result_multi = b_item_t * b_item_f
print('b_item_result_multi =',b_item_result_multi)

#b_item_result_division = b_item_t / b_item_f
#print('b_item_result_division =',b_item_result_division)

b_item_1_int = int(b_item_t)
print('b_item_1_int =',b_item_1_int)

b_item_2_int = int(b_item_f)
print('b_item_2_int =',b_item_2_int)
