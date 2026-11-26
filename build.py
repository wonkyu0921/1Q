"""src/estimate.html + 로고 → dist/견적서.html (단독 실행용) 생성"""
import base64, pathlib
root = pathlib.Path(__file__).parent
body = (root / "src/estimate.html").read_text(encoding="utf-8")
logo = base64.b64encode((root / "src/logo.png").read_bytes()).decode()
body = body.replace("__LOGO__", logo)
(root / "dist").mkdir(exist_ok=True)
(root / "dist/artifact.html").write_text(body, encoding="utf-8")
head = '<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">'
(root / "견적서.html").write_text(head + body + "</body></html>", encoding="utf-8")
print("built")
