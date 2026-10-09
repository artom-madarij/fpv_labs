# Лабораторна робота №2

**Тема:** Моделювання безпілотних систем у Gazebo та ArduPilot SITL.

**Група:** ІР-34
**Варіант:** 37

## Що зроблено

- Підняв Gazebo + ArduPilot SITL + ROS 2 Humble.
- Зробив скрипт `~/run_sim.sh` щоб не вводити купу команд щоразу.
- Запустив початковий приклад `flight_test` — дрон злітає, висить 30 сек і сідає.
- Написав свій вузол `flight_target` — дрон летить до заданої точки і сідає там.

## Структура проєкту
```
fpv_lab2/
 ├── init.py
 ├── flight_state.py 
 ├── flight_test_node.py 
 ├── main.py # запуск flight_test
 ├── flight_target_node.py 
 ├── flight_target_main.py
 └── handlers/
       ├── init.py 
       ├── handler.py 
       ├── waiting_for_system.py 
       ├── prearm_check.py 
       ├── setting_guided.py 
       ├── arming.py 
       ├── taking_off.py 
       ├── hovering.py 
       ├── landing.py 
       ├── waiting_for_landing.py 
       ├── going_to_target.py 
       └── target_hovering.py 
```
## Параметри

Варіант 37 по методичці: Δx = 4.0, Δy = −0.4.

Але в лабіринті ціль попадала на стінку, тому трохи підправив:

- Δx: 4.0 → **3.5**
- висота зльоту: 2.0 → **5.0 м** (щоб летіти над стінами)

Δy залишив як є (−0.4).

## Результат

- Старт: (0.00, 0.00)
- Ціль: (−3.50, 0.40)
- Сів з похибкою **0.30 м**
