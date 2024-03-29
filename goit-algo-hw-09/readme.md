# Порівняння ефективності алгоритмів для розбиття суми на монети

У данному дослідженні порівняли ефективність двох алгоритмів - жадібного алгоритму та алгоритму динамічного програмування - для вирішення задачі розбиття суми на монети. Обидва алгоритми мають свої переваги та недоліки, і їх ефективність залежить від розміру вхідних даних.

## Результати виконання алгоритмів

| Сума       | Жадібний, сек                  | Динамічний, сек                | Різниця                        |
| ---------- | ------------------------------ | ------------------------------ | ------------------------------ |
| 10         | 1.1799857020378113e-05         | 8.33999365568161e-05           | -7.160007953643799e-05         |
| 100        | 1.0599847882986069e-05         | 0.0007162999827414751          | -0.000705700134858489          |
| 1000       | 1.0800082236528397e-05         | 0.008465099846944213           | -0.008454299764707685          |
| 10000      | 1.2100208550691605e-05         | 0.09260550001636147            | -0.09259339980781078           |
| 100000     | 1.2399861589074135e-05         | 1.0811270999256521             | -1.081114700064063             |

## Аналіз результатів

1. **Жадібний алгоритм:**
   - **Переваги:** Швидше для менших сум, працює добре, коли оптимальність не є головним критерієм.
   - **Недоліки:** Може давати неоптимальні результати для великих сум.

2. **Алгоритм динамічного програмування:**
   - **Переваги:** Забезпечує оптимальний результат для будь-якої суми, особливо важливо для великих сум.
   - **Недоліки:** Вимагає більше часу, особливо для великих вхідних даних.

## Висновки

- **Жадібний алгоритм:** Підходить для невеликих сум, де важлива швидкість, і оптимальність не є критичною.
  
- **Алгоритм динамічного програмування:** Забезпечує оптимальний результат для будь-якої суми, особливо важливо для великих сум, але вимагає більше часу.

Вибір між цими алгоритмами залежить від конкретних вимог задачі та розміру вхідних даних.
