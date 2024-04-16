# SIiIW_zad_1

## Sztuczna inteligencja i inżynieria wiedzy Lista 1

Celem ćwiczenia jest praktyczne zapoznanie się z problemami optymalizacyjnymi
oraz praktyczne przećwiczenie omawianych na wykładzie metod rozwiązywania pewnej
podklasy tych problemów.  
Po wykonaniu listy, student powinien wiedzieć czym jest problem optymalizacyjny,
jakie trudności mogą się wiązać z uzyskaniem dokładnego
rozwiązania przedstawionego problemu oraz jak po radzić sobie z rozwiązaniem problemu
przy ograniczonych zasobach (np. moce obliczeniowe, czas).  
W szczególności znane powinny
być różnice między aproksymacją a heurystyką oraz przykłady podejścia heurystycznego do
problemu przeszukania, oraz znajdowania ścieżek.

## 2  Wprowadzenie teoretyczne

znajdują się informacje pomocne w wykonaniu listy zadań.  
Zakłada się, że po wykonaniu student opanował zagadnienia teoretyczne.

### 2.1 Definicje Definicja 1 (Problem Optymalizacyjny)

Problemem optymalizacyjnym nazywamy zbiór ograniczeń (zadanych w postaci nierówności lub
równości na zmiennych decyzyjnych) wraz z funkcją celu.
Niech S będzie zbiorem rozwiązań dopuszczalnych w założonym problemie, tzn. zbiór takich  ̄x,
które spełniają wszystkie ograniczenia, a `f( ̄x) : Kn → K` funkcją oceny jakości rozwiązania.
Wtedy problemem minimalizacyjnym nazywamy znalezienie takiego `s∗ ∈ S`,
dla którego `s∗ = mins∈S f(s)` a `f(s)` jest funkcją kosztu.
Alternatywnie, problem nazywamy maksymalizacyjnym jeśli celem jest
znalezienie takiego `s∗ ∈ S`, dla którego `s∗ = maxs∈S f(s)` a `f(s)` jest funkcją użyteczności.
Łatwo zauważyć, że dowolny problem minimalizacyjny można zamienić na maksymalizacyjny.
