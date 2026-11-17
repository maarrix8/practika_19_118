results = [5, 0, 7, 5, 2]
results.append(10)
results.insert(3,3)
print("ESLi CHT0:O",results)
results[0] = 5
removed = results.pop()
print("Измененный список:", results)
print("Удаленный элемент:", removed)
total_sum = 0
for num in results:
    total_sum += num
print("Сумма элементов списка:", total_sum)
sorted_results =sorted(results,reverse=True)
print("Отсортированная копия:", sorted_results)
print("Исходный список :", results)
results_tuple = tuple(results)
print( results_tuple)
print(results_tuple[0])
print( results_tuple[-1])