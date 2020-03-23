def counting(arr):
    max_elem = max(arr) + 1
    count = [0] * max_elem
      
    for element in arr:
        count[element] += 1
 
    result = []
    for element in arr:
        if count[element] == 1:
            result.append(element)
    return result