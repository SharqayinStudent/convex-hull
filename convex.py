def cross(o, a, b):
    """Вычисляет векторное произведение векторов OA и OB.
    Положительное значение — поворот против часовой стрелки,
    отрицательное — по часовой стрелке, 0 — если точки коллинеарны."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    # Сортировка точек лексикографически (сначала по x, потом по y)
    points = sorted(points)

    # Построение нижней оболочки
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()  # Убираем точку, если поворот не в нужную сторону
        lower.append(p)

    # Построение верхней оболочки
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Убираем последнюю точку из верхней оболочки, так как она уже включена в нижнюю
    return lower[:-1] + upper[:-1]

# Пример использования
points = [(0, 0), (1, 1), (2, 2), (2, 0), (3, 1), (3, 3), (0, 3)]
hull = convex_hull(points)

print("Конвексная оболочка:", hull)
