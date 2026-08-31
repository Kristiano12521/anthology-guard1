# Карточка лога — xray_barkid.log

- Файл: `xray_barkid.log` (4.4 МБ, 67731 строк)
- Дата разбора: 2026-08-31
- Класс: **вылета нет, есть повторяющиеся ошибки (2 групп)**
- Среда: xrCore build 10057, anomalydx11avx.exe

## Нефатальные ошибки

### 1. `axr_main.script` ×19

Триггер: `![axr_main callback_set] trying to set callback actor_on_item_use to nil function!`

```
... axr_main.script (line: 253) in function 'callback_set'
... _g.script (line: 104) in function 'RSC'
... dxml_core.script (line: 27) in function 'RegisterScriptCallback'
... mas_scope_detach.script (line: 106) in function 'on_game_start'
... axr_main.script (line: 359) in function 'on_game_start'
... _g.script (line: 82) in function <... _g.script:73>
```

### 2. `sound_theme.script` ×9

Триггер: нет строки с `!` / `~` перед блоком

```
... _g.script (line: 672) in function 'abort'
... sound_theme.script (line: 644) in function <... sound_theme.script:614>
[C]: in function 'object_sound'
... sound_theme.script (line: 877) in function <... sound_theme.script:868>
[C]: in function 'section_for_each'
... sound_theme.script (line: 885) in function 'load_sound'
... bind_stalker.script (line: 107) in function <... bind_stalker.script:100>
[C]: in function 'actor_binder'
... bind_stalker.script (line: 6) in function <... bind_stalker.script:5>
```

## Куда смотреть

- Блок FATAL ERROR не найден, но есть 28 нефатальных Lua-ошибок, 2 уникальных сигнатур.
- Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.
- Самая частая: `axr_main.script` ×19.

## Последние строки лога (40)

```
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.13/0.00/0.00/5.17/5.16/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.13 ms gc(calls/busy/postload)=1980/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.35/0.24/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.37/1.35/0.00 ms max(total/frame/render/wait)=5.93/0.72/0.00/0.28 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.14/0.00/0.00/5.18/5.16/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.12 ms gc(calls/busy/postload)=1839/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.35/0.26/0.00/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.06/0.00/0.00/1.33/1.31/0.00 ms max(total/frame/render/wait)=6.28/1.57/0.00/0.64 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.14/0.00/0.00/5.46/5.44/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.29 ms gc(calls/busy/postload)=1949/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.33/0.27/0.00/0.02 ms workers(pre/post/bones/game/lua-gc/vision)=0.06/0.00/0.00/1.41/1.39/0.00 ms max(total/frame/render/wait)=10.67/2.34/0.00/5.41 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.18/0.00/0.00/8.24/8.21/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.24 ms gc(calls/busy/postload)=1828/1/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.37/0.28/0.00/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.06/0.00/0.00/1.35/1.33/0.00 ms max(total/frame/render/wait)=13.04/5.08/0.00/1.79 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.18/0.00/0.00/5.28/5.26/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.06 ms gc(calls/busy/postload)=1878/2/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.33/0.21/0.00/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.34/1.32/0.00 ms max(total/frame/render/wait)=6.41/0.64/0.00/2.59 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.19/0.00/0.00/5.99/5.96/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.17 ms gc(calls/busy/postload)=1967/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.29/0.20/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.33/1.32/0.00 ms max(total/frame/render/wait)=5.92/0.56/0.00/0.01 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.15/0.00/0.00/4.88/4.87/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.05 ms gc(calls/busy/postload)=1972/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.33/0.22/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.34/1.33/0.00 ms max(total/frame/render/wait)=5.93/2.17/0.00/0.48 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.13/0.00/0.00/5.14/5.13/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.04 ms gc(calls/busy/postload)=1907/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.32/0.20/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.04/0.00/0.00/1.28/1.27/0.00 ms max(total/frame/render/wait)=5.92/0.47/0.00/0.42 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.11/0.00/0.00/4.82/4.80/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.03 ms gc(calls/busy/postload)=1991/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.32/0.22/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.37/1.35/0.00 ms max(total/frame/render/wait)=5.92/0.55/0.00/0.21 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.09/0.00/0.00/5.50/5.48/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.03 ms gc(calls/busy/postload)=1868/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.33/0.25/0.00/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.33/1.31/0.00 ms max(total/frame/render/wait)=6.31/5.40/0.00/0.67 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.15/0.00/0.00/5.33/5.31/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.01 ms max=0.00/0.00/0.05 ms gc(calls/busy/postload)=1979/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.34/0.25/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.06/0.00/0.00/1.36/1.34/0.00 ms max(total/frame/render/wait)=5.91/0.61/0.00/0.47 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.22/0.00/0.00/5.32/5.31/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.05 ms gc(calls/busy/postload)=1864/0/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.27/0.25/0.00/0.01 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.34/1.33/0.00 ms max(total/frame/render/wait)=5.92/1.90/0.00/1.45 ms
* [mt-frame/profile] max-workers(pre/post/bones/game/lua-gc/vision)=0.18/0.00/0.00/4.91/4.90/0.00 ms
* [mt-frame/profile] game-breakdown avg(scheduler/parallel/frame-mt)=0.00/0.00/0.02 ms max=0.00/0.00/0.05 ms gc(calls/busy/postload)=1867/2/0
* [mt-frame/profile] frames=300 avg(total/frame/render/wait)=5.32/0.22/0.00/0.00 ms workers(pre/post/bones/game/lua-gc/vision)=0.05/0.00/0.00/1.32/1.30/0.00 ms max(total/frame/render/wait)=6.22/1.15/0.00/0.55 ms
* [mt-frame/profile] max-w
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
