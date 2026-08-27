# MCM

Mod Configuration Menu — штатное место для настроек мода в Anomaly 1.5.3. Хардкод констант в скрипте вместо MCM запрещён правилами проекта: настройку, которую нельзя поменять из игры, придётся править файлом, а это конфликт при каждом обновлении мода.

## Контракт

MCM сканирует `gamedata/scripts` на файлы, чьё имя заканчивается на `mcm.script`, и вызывает в них `on_mcm_load()`. Функция возвращает дерево опций.

```lua
-- my_mod_mcm.script
function on_mcm_load()
    return {
        id = "my_mod",          -- уникальный идентификатор мода
        sh = true,              -- сворачиваемый раздел
        gr = {
            {id = "enable",    type = "check", val = 1, def = true,
             text = "ui_mcm_my_mod_enable"},

            {id = "intensity", type = "track", val = 2,
             min = 0, max = 1, step = 0.05, def = 0.5,
             text = "ui_mcm_my_mod_intensity"},

            {id = "hotkey",    type = "key_bind", val = 2, def = DIK_keys.DIK_F7,
             text = "ui_mcm_my_mod_hotkey"},

            {id = "mode",      type = "list", val = 2, def = 0,
             text = "ui_mcm_my_mod_mode",
             content = {
                 {0, "ui_mcm_my_mod_mode_off"},
                 {1, "ui_mcm_my_mod_mode_soft"},
                 {2, "ui_mcm_my_mod_mode_hard"},
             }},
        }
    }
end
```

`val` обязателен: `1` для boolean-опций, `2` для числовых и значений из списка. Пропущенный `val` роняет `ui_mcm.script` при открытии меню — это одна из самых частых ошибок в чужих модах.

## Чтение значений

```lua
local function opt(path, default)
    return ui_mcm and ui_mcm.get(path) or default
end

local enabled = opt("my_mod/enable", true)
```

Проверка `ui_mcm` обязательна: без неё мод падает у игрока без MCM. Дефолт в коде должен совпадать с `def` в дереве опций — иначе поведение «до открытия меню» и «после» будет разным.

Значения читаем в момент использования. Кэширование при загрузке скрипта означает, что изменение настройки не применится до перезапуска.

## Тексты

`text` — ключ строковой таблицы, а не готовая строка. Ключи кладём в `gamedata/configs/text/<lang>/ui_st_mcm_<mod_id>.xml`:

```xml
<?xml version="1.0" encoding="windows-1251"?>
<string_table>
    <string id="ui_mcm_my_mod">
        <text>My Mod</text>
    </string>
    <string id="ui_mcm_my_mod_enable">
        <text>Enable</text>
    </string>
</string_table>
```

Файл в Windows-1251, кодировка объявлена в шапке. Как минимум `eng`, при необходимости `rus`.

## Разделение файлов

`<mod_id>_mcm.script` описывает только дерево опций. Игровая логика — в `<mod_id>.script`. Иначе при ошибке в логике падает регистрация настроек, и мод исчезает из меню целиком, что сильно затрудняет диагностику.

## Стабильность идентификаторов

`id` мода и `id` опции — это ключ, по которому MCM хранит выбор игрока. Их переименование сбрасывает настройки у всех, кто уже поставил мод. Меняем только при явной необходимости и с записью в `CHANGELOG.md`.
