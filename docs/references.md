# Внешние источники

Порядок доверия тот же, что в [`api-verification.md`](api-verification.md): исходники сборки важнее любой из этих ссылок. Всё отсюда проверяется по `reference/`, потому что версии и сборки различаются.

## Cursor

- [Rules — официальная документация](https://cursor.com/docs/rules) — форматы `.mdc`, четыре режима активации, `AGENTS.md`. Ключевое: `.cursorrules` устарел; обычный `.md` в `.cursor/rules/` игнорируется; документированный формат `globs` — строка через запятую.

## Anomaly: движок и exe

- [themrdemonized/xray-monolith](https://github.com/themrdemonized/xray-monolith) — Modded Exes, включая MT-ветку. README — источник истины по тому, что именно многопоточно, какие консольные переменные и тумблеры существуют, какие функции добавлены к ванильному API.

## Anomaly: скрипты и конфиги

- [S.T.A.L.K.E.R. Anomaly Modding Guide](https://robe127.github.io/stalker-anomaly-modding-guide/) — система callback'ов, жизненный цикл скриптов, область видимости, MCM, DLTX. Наиболее аккуратный современный справочник.
- [anomaly-modding-book](https://github.com/TheParaziT/anomaly-modding-book) — туториалы по DLTX, MCM, monkey-patching.
- [DLTX — Differential LTX Loading](https://aqxaromods.com/stalker/anomaly/2190-dltx-differential-ltx-loading-updated-25th-september-2021.html) — исходное описание механизма от автора.
- [RAX-Anomaly/Anomaly-Mod-Configuration-Menu](https://github.com/RAX-Anomaly/Anomaly-Mod-Configuration-Menu) — исходники MCM и описание дерева опций.

## Инструменты

- Mod Organizer 2 — виртуальная файловая система и порядок загрузки; вкладка Conflicts у мода показывает, кто кого перекрывает.

## Чего избегать

Гайды по Call of Chernobyl, Call of Misery, OGSR, IX-Ray и чистому CoP выглядят применимо, но API расходится. Использовать только как подсказку, где искать, а не как готовый код.
