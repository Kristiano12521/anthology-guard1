# Карточка лога — xray_nikit.log

- Файл: `xray_nikit.log` (560 КБ, 8635 строк)
- Дата разбора: 2026-08-31
- Класс: **вылета в логе нет**
- Среда: xrCore build 10063, anomalydx11avx.exe

## Куда смотреть

- Блок FATAL ERROR не найден: либо лог от нормального сеанса, либо игра упала без записи (проверь конец файла вручную).

## Предупреждения (топ 15)

- x4 `! [12:21:29.N] ERROR item_combination | wrong section names`
- x4 `~ [12:21:39.N]  ------------------------------------------------------------------------`
- x2 `! [12:20:26.N]  Can't find sound 'material\human\step\n_default_5'`
- x2 `! [12:20:26.N]  Can't find sound 'material\human\step\n_default_6'`
- x2 `! [12:20:26.N]  Can't find sound 'material\human\step\n_gravel_6'`
- x2 `! [12:20:26.N]  Can't find sound 'material\human\step\n_gravel_5'`
- x2 `! [12:20:26.N]  Can't find sound 'material\actor\step\n_gravel_5'`
- x2 `! [12:20:26.N]  Can't find sound 'material\actor\step\n_gravel_6'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_conc_h_01'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_conc_h_02'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_conc_h_03'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_conc_h_04'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_dirt_h_01'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_dirt_h_02'`
- x2 `! [12:20:26.N]  Can't find sound 'material\shells\small_shell_dirt_h_03'`

## Последние строки лога (40)

```
* [12:36:11.607]         :   1: ui\ui_options
* [12:36:11.607]         :   1: ui\ui_rak_global_1
* [12:36:11.607]         :   1: ui\ui_rak_global_2
* [12:36:11.607]         :   1: ui\ui_rak_global_ammo
* [12:36:11.607]         :   1: ui\ui_rak_global_device
* [12:36:11.607]         :   1: ui\ui_rak_global_knife
* [12:36:11.607]         :   1: ui\ui_stalker2_armors
* [12:36:11.607]         :   1: ui\ui_stalker2_mutantparts
* [12:36:11.607]         :   1: unrealengine\electricblast1
* [12:36:11.607]         :   1: unrealengine\electricblast2
* [12:36:11.607]         :   1: unrealengine\puffcolorsplashflicker
* [12:36:11.607]  RM_Dump: rtargets  : 0
* [12:36:11.607]  RM_Dump: vs        : 3
* [12:36:11.607]         :  30: particle
* [12:36:11.607]         :  26: particle-clip
* [12:36:11.607]         :  23: stub_notransform_t
* [12:36:11.607]  RM_Dump: ps        : 7
* [12:36:11.607]         :  22: hud_default
* [12:36:11.607]         :  26: particle
* [12:36:11.607]         :   4: particle_distort
* [12:36:11.607]         :   9: particle_s-aadd
* [12:36:11.607]         :   5: particle_s-add
* [12:36:11.607]         :  12: particle_s-blend
* [12:36:11.607]         :   1: stub_default
* [12:36:11.607]  RM_Dump: dcl       : 1
* [12:36:11.607]  RM_Dump: states    : 7
* [12:36:11.607]  RM_Dump: tex_list  : 53
* [12:36:11.607]  RM_Dump: matrices  : 0
* [12:36:11.607]  RM_Dump: lst_constants: 0
* [12:36:11.607]  RM_Dump: v_passes  : 79
* [12:36:11.607]  RM_Dump: v_elements: 79
* [12:36:11.607]  RM_Dump: v_shaders : 53
[12:36:11.624] refCount:pBaseZB 1
[12:36:11.624] refCount:pBaseRT 1
[12:36:11.703] refCount:m_pSwapChain 1
[12:36:11.703] DeviceREF: 268
[12:36:11.703] refCount:m_pOutput 2
[12:36:11.703] refCount:m_pAdapter 2
[12:36:11.703] refCount:m_pFactory 2
[12:36:11.829] [xrLogger] InternalCloseLog called, terminating thread
```

---

Разбор ведём по `workflow-crash`: сначала класс и первопричина, фикс — только после подтверждения.
