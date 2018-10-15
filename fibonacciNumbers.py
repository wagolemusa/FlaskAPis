class fibNumbers:
  def fibonaccil(self, number):
    num = [1,2]
    for i in range (2, number):
      num.append(num[i-2]+num[i-1])
    return num
  
  def sum_even_fibonaccil(self, number=1000):
    sum = 0
    for i in self.fibonaccil(number):
      if i % 2 == 0 and i < 4000000:
        sum  = sum+i
    return sum

test = fibNumbers()
print (test.sum_even_fibonaccil())


# class fibonacciNumbers:
#     def fibonacci(self, number):
#         output = [1,2]
#         for each in range(2,number):
#             output.append(output[each-2]+output[each-1])
#         return output

#     def sum_of_even_fibonacci(self, number=1000):
#         sum = 0
#         for each in self.fibonacci(number):
#             if each%2 == 0 and each<4000000:
#                 sum = sum+each
#         return sum
        
# if __name__ == '__main__':
#     test = fibonacciNumbers()
#     print (test.sum_of_even_fibonacci())