def add_bonus(scores, bonus):
    """Orijinal siyahını birbaşa dəyişir (bonus əlavə edir)."""
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)
def with_bonus(scores, bonus):
    """Orijinal siyahıya toxunmur, yeni siyahı yaradıb qaytarır."""
    new_scores = []
    for score in scores:
        new_scores.append(min(100, score + bonus))
    return new_scores
scores = [70, 95, 88, 100]
print("Orijinal siyahı:", scores)
print("with_bonus nəticəsi (yeni siyahı):", with_bonus(scores, 10))
print("Orijinal siyahı hələ də dəyişməyib:", scores)
add_bonus(scores, 10)
print("add_bonus işlədikdən sonra orijinal siyahı dəyişdi:", scores)