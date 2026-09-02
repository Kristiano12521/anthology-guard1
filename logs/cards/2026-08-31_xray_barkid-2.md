# Карточка лога — xray_barkid (1).log

- Файл: `xray_barkid (1).log` (5.4 МБ, 84021 строк)
- Дата разбора: 2026-08-31
- Класс: **вылета нет, есть повторяющиеся ошибки (2 групп)**
- Среда: xrCore build 10057, anomalydx11avx.exe

## Нефатальные ошибки

### 1. `axr_main.script` ×23

Триггер: `![axr_main callback_set] trying to set callback actor_on_item_use to nil function!`

```
... axr_main.script (line: 253) in function 'callback_set'
... _g.script (line: 104) in function 'RSC'
... dxml_core.script (line: 27) in function 'RegisterScriptCallback'
... mas_scope_detach.script (line: 106) in function 'on_game_start'
... axr_main.script (line: 359) in function 'on_game_start'
... _g.script (line: 82) in function <... _g.script:73>
```

### 2. `sound_theme.script` ×13

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

- Блок FATAL ERROR не найден, но есть 36 нефатальных Lua-ошибок, 2 уникальных сигнатур.
- Смотри секцию «Нефатальные ошибки»: повторяющиеся traceback'и — основной класс проблем этой сборки.
- Самая частая: `axr_main.script` ×23.

## Последние строки лога (40)

```
~ ------------------------------------------------------------------------
~ ------------------------------------------------------------------------
There are no sound collection with path: semitone\anomalies\generators
Time continual is:7770838
# LOADING: level_weather | cycle: clear - preset: w_cloudy3 - is_underground: true - weather_storage size: 7
WeatherManager.load_state is underground, skip
* [load-session/actor-spawn-addon] native phantom scan=0 ms
article: processing article_opo
article: processing articles_exo
article: processing articles_wpo
article: processing article_opo
article: processing articles_exo
article: processing articles_wpo
-Smart terrains can spawn squads normaly
- TB_Remove_Bugged_Stashes script has already been run in this game.
[id_cleaner_anthology] on_game_load: initialized=true
[WG] Western Goods version 3.1.0
g_game_difficulty gd_veteran
g_hit_pwr_modif 1
g_dispersion_base 1.3
g_dispersion_factor 1.5
- Water deprivation | Enabled
- Sleep deprivation | Enabled
[G2X_Writer] Successfully written config: c:/games/anthology/anomaly-1.5.3-anthology 2.1/bin/..\gamedata\configs\mod_system_z_ref_torch_definition.ltx
[G2X_Writer] Successfully written config: c:/games/anthology/anomaly-1.5.3-anthology 2.1/bin/..\gamedata\configs\mod_system_z_red_flashlight_definition.ltx
[G2X_Writer] Successfully written config: c:/games/anthology/anomaly-1.5.3-anthology 2.1/bin/..\gamedata\configs\mod_system_position_fix.ltx
* [load-session/lua-callbacks] on_game_load total=154.26 ms callbacks=83
* [load-session/lua-callbacks] #01 self=82.88 ms source=...gy 2.1/bin/..\gamedata\scripts\western_goods_core.script:129
* [load-session/lua-callbacks] #02 self=58.69 ms source=...bin/..\gamedata\scripts\western_goods_ui_readable.script:130
* [load-session/lua-callbacks] #03 self=3.78 ms source=...y 2.1/bin/..\gamedata\scripts\z_nta_stashes_utils.script:4
* [load-session/lua-callbacks] #04 self=2.02 ms source=...2.1/bin/..\gamedata\scripts\g2x_mcm_config_writer.script:101
* [load-session/lua-callbacks] #05 self=1.64 ms source=...1/bin/..\gamedata\scripts\ui_pda_encyclopedia_tab.script:517
* [load-session/lua-callbacks] #06 self=1.50 ms source=...-anthology 2.1/bin/..\gamedata\scripts\txr_routes.script:3056
* [load-session/lua-callbacks] #07 self=0.95 ms source=...2.1/bin/..\gamedata\scripts\arszi_mutant_bleeding.script:45
* [load-session/lua-callbacks] #08 self=0.66 ms source=...n/..\gamedata\scripts\modxml_zzz_rand_text_dialog.script:68
* [load-session/lua-callbacks] #09 self=0.33 ms source=...ogy 2.1/bin/..\gamedata\scripts\game_difficulties.script:161
* [load-session/lua-callbacks] #10 self=0.30 ms source=...hology 2.1/bin/..\gamedata\scripts\game_relations.script:532
* [load-session/lua-callbacks] #11 self=0.25 ms source=...n/..\gamedata\scripts\liz_fdda_redone_consumables.script:310
* [load-session/lua-callbacks] #12 self=0.22 ms source=...anthology 2.1/bin/..\gamedata\scripts\haru_skills.script:292
* [load-session/lua-callbacks] #13 self=0.16 ms source=...nthology 2.1/bin/..\gamedata\scripts
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
