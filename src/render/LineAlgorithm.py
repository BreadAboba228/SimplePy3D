def draw_line(buffer: list[list[str]], 
               start: tuple[int, int], 
               end: tuple[int, int],
               width: int,
               height: int,
               symbol: str) -> list[list[str]]:


    x1, y1 = start
    x2, y2 = end

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    error = delta_x - delta_y

    while True:
        if 0 <= x1 < width and 0 <= y1 < height:
            buffer[y1][x1] = symbol
        
        if x1 == x2 and y1 == y2:
            break

        error2 = error * 2

        if error2 > -delta_y:
            error -= delta_y
            x1 += step_x
        
        if error2 < delta_x:
            error += delta_x
            y1 += step_y

    return buffer