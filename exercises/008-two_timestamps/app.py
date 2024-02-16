def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    total_hr = hr2 - hr1 
    total_min = min2 - min1
    total_sec = sec2 - sec1

    hr_to_sec = total_hr * 3600
    min_to_sec = total_min * 60 

    result = hr_to_sec + min_to_sec + total_sec
    return result


print(two_timestamp(1,1,1,2,2,2))
