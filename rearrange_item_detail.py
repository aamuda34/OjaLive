path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    <div style="padding:18px 16px 16px;border-radius:20px 20px 0 0;background:#fff;position:relative;margin-top:-16px;">
      <div id="bd-category" style="font-size:11px;color:var(--earth);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;"></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:6px;">
        <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);line-height:1.25;flex:1;"></div>
        <div id="bd-badge" style="flex-shrink:0;margin-top:2px;"></div>
      </div>
      <div id="bd-inline-rating" style="font-size:12px;color:var(--muted);margin-bottom:10px;display:none;"></div>
      <div style="display:flex;align-items:baseline;gap:6px;margin-bottom:10px;">
        <div id="bd-price" style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--earth);"></div>
        <div id="bd-unit" style="font-size:13px;color:var(--muted);"></div>
      </div>
      <div id="bd-stock" style="display:none;background:#E8F5EE;color:var(--green);font-size:12px;font-weight:600;padding:6px 12px;border-radius:8px;margin-bottom:4px;"></div>
      <!-- SELLER INFO -->
      <div style="background:#FAF7F2;border:1px solid var(--border);border-radius:14px;padding:14px;margin:14px 0;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div id="bd-seller-photo" style="width:48px;height:48px;border-radius:50%;background:var(--earth);color:#fff;font-size:19px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-weight:700;"></div>
          <div style="flex:1;min-width:0;">
            <div style="display:flex;align-items:center;gap:6px;">
              <div id="bd-trader" style="font-size:14px;font-weight:700;color:var(--dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"></div>
              <div id="bd-seller-inline-rating" style="font-size:11px;color:#F59E0B;font-weight:700;flex-shrink:0;display:none;"></div>
            </div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);"></div>
          </div>
          <button id="bd-follow-btn2" onclick="toggleFollow()" style="padding:7px 14px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:11px;font-weight:700;cursor:pointer;flex-shrink:0;">+ Follow</button>
        </div>
        <div style="margin-top:10px;padding-top:10px;border-top:1px solid var(--border);display:flex;flex-direction:column;gap:4px;">
          <div id="bd-location" style="font-size:12px;color:var(--muted);"></div>
          <div id="bd-hours" style="font-size:11px;color:var(--green);"></div>
          <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;"></div>
        </div>
      </div>
      <!-- ITEM DESCRIPTION -->
      <div id="bd-description" style="display:none;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:8px;">About this item</div>
        <div id="bd-desc-text" style="font-size:13px;color:var(--dark);line-height:1.6;"></div>
      </div>
      <!-- SELLER DESCRIPTION -->
      <div id="bd-seller-desc" style="display:none;margin-top:8px;padding-top:8px;border-top:1px solid var(--border);">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:4px;">About the seller</div>
        <div id="bd-seller-desc-text" style="font-size:12px;color:var(--muted);font-style:italic;line-height:1.5;"></div>
      </div>
      <button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:14px;align-items:center;justify-content:center;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>Chat Now</button>
      <!-- REVIEWS & RATINGS -->'''

new = '''    <div style="padding:18px 16px 16px;border-radius:20px 20px 0 0;background:#fff;position:relative;margin-top:-16px;">
      <div id="bd-category" style="font-size:11px;color:var(--earth);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;margin-bottom:6px;"></div>
      <div id="bd-name" style="font-family:'Syne',sans-serif;font-size:19px;font-weight:800;color:var(--dark);line-height:1.25;margin-bottom:4px;"></div>
      <div id="bd-inline-rating" style="font-size:12px;color:var(--muted);margin-bottom:10px;display:none;"></div>
      <div style="display:flex;align-items:baseline;gap:8px;margin-bottom:10px;flex-wrap:wrap;">
        <div id="bd-price" style="font-family:'Syne',sans-serif;font-size:26px;font-weight:800;color:var(--earth);"></div>
        <div id="bd-unit" style="font-size:13px;color:var(--muted);"></div>
        <div id="bd-badge" style="margin-left:auto;flex-shrink:0;"></div>
      </div>
      <div id="bd-stock" style="display:none;background:#E8F5EE;color:var(--green);font-size:12px;font-weight:600;padding:6px 12px;border-radius:8px;margin-bottom:14px;width:fit-content;"></div>
      <!-- ITEM DESCRIPTION -->
      <div id="bd-description" style="display:none;background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:14px;">
        <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:8px;">About this item</div>
        <div id="bd-desc-text" style="font-size:13px;color:var(--dark);line-height:1.6;"></div>
      </div>
      <!-- SELLER INFO -->
      <div style="background:#FAF7F2;border:1px solid var(--border);border-radius:14px;padding:14px;margin-bottom:14px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <div id="bd-seller-photo" style="width:48px;height:48px;border-radius:50%;background:var(--earth);color:#fff;font-size:19px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-weight:700;"></div>
          <div style="flex:1;min-width:0;">
            <div style="display:flex;align-items:center;gap:6px;">
              <div id="bd-trader" style="font-size:14px;font-weight:700;color:var(--dark);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;"></div>
              <div id="bd-seller-inline-rating" style="font-size:11px;color:#F59E0B;font-weight:700;flex-shrink:0;display:none;"></div>
            </div>
            <div id="bd-followers-count" style="font-size:11px;color:var(--muted);"></div>
          </div>
          <button id="bd-follow-btn2" onclick="toggleFollow()" style="padding:7px 14px;background:var(--earth);color:#fff;border:none;border-radius:20px;font-size:11px;font-weight:700;cursor:pointer;flex-shrink:0;">+ Follow</button>
        </div>
        <div style="margin-top:10px;padding-top:10px;border-top:1px solid var(--border);display:flex;flex-direction:column;gap:4px;">
          <div id="bd-location" style="font-size:12px;color:var(--muted);"></div>
          <div id="bd-hours" style="font-size:11px;color:var(--green);"></div>
          <div id="bd-dist" style="font-size:11px;color:var(--green);font-weight:600;"></div>
        </div>
        <!-- SELLER DESCRIPTION -->
        <div id="bd-seller-desc" style="display:none;margin-top:10px;padding-top:10px;border-top:1px solid var(--border);">
          <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;margin-bottom:4px;">About the seller</div>
          <div id="bd-seller-desc-text" style="font-size:12px;color:var(--muted);font-style:italic;line-height:1.5;"></div>
        </div>
      </div>
      <button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:14px;align-items:center;justify-content:center;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>Chat Now</button>
      <!-- REVIEWS & RATINGS -->'''

stock_old = "if(item.stock){stockEl.style.display='flex';stockEl.style.alignItems='center';stockEl.innerHTML='<svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"margin-right:6px;flex-shrink:0;\"><path d=\"M21 8l-9-5-9 5 9 5 9-5z\"/><path d=\"M3 8v8l9 5 9-5V8\"/><path d=\"M12 13v8\"/></svg>'+item.stock+' units available';}"
stock_new = "if(item.stock){stockEl.style.display='inline-flex';stockEl.style.alignItems='center';stockEl.innerHTML='<svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"margin-right:6px;flex-shrink:0;\"><path d=\"M21 8l-9-5-9 5 9 5 9-5z\"/><path d=\"M3 8v8l9 5 9-5V8\"/><path d=\"M12 13v8\"/></svg>'+item.stock+' units available';}"

count = 0
if old in content:
    content = content.replace(old, new, 1)
    count += 1
else:
    print("WARNING: layout block not found — file may already differ from expected")

if stock_old in content:
    content = content.replace(stock_old, stock_new, 1)
    count += 1
else:
    print("WARNING: stock-chip JS not found — skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/2 replacements applied.")
