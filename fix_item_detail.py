path = "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
("""<button onclick="closeBuyerDetail()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);">\u2190</button>
      <button onclick="shareItem()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);">\u2934</button>""",
"""<button onclick="closeBuyerDetail()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg></button>
      <button onclick="shareItem()" style="background:rgba(0,0,0,0.4);backdrop-filter:blur(6px);border:none;color:#fff;width:38px;height:38px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.6" y1="10.5" x2="15.4" y2="6.5"/><line x1="8.6" y1="13.5" x2="15.4" y2="17.5"/></svg></button>"""),

('<button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:14px;">\U0001F4AC Chat Now</button>',
 '<button id="bd-chat-btn" style="display:none;width:100%;padding:14px;background:var(--earth);color:#fff;border:none;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;margin-bottom:14px;align-items:center;justify-content:center;gap:8px;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>Chat Now</button>'),

("""      <!-- REVIEWS -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">Reviews</div>
          <div id="bd-avg-rating" style="font-size:13px;font-weight:700;color:var(--earth);"></div>
        </div>
        <div id="bd-reviews-list"><div style="font-size:13px;color:var(--muted);text-align:center;padding:10px;">No reviews yet. Be the first!</div></div>
        <div style="margin-top:12px;border-top:1px solid var(--border);padding-top:12px;">
          <div style="font-size:12px;font-weight:600;color:var(--dark);margin-bottom:8px;">Write a Review</div>
          <div id="bd-star-rating" style="display:flex;gap:6px;margin-bottom:8px;font-size:24px;">
            <span onclick="setReviewRating(1)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(2)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(3)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(4)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(5)" style="cursor:pointer;" class="star">\u2606</span>
          </div>
          <textarea id="bd-review-text" placeholder="Share your experience with this item..." style="width:100%;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:70px;font-family:inherit;margin-bottom:8px;"></textarea>
          <input type="text" id="bd-reviewer-name" placeholder="Your name (optional)" style="margin-bottom:8px;font-size:13px;">
          <button onclick="submitReview()" style="width:100%;padding:10px;background:var(--earth);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Review</button>
        </div>
      </div>
      <!-- SELLER RATING -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">Rate this Seller</div>
          <div id="bd-seller-avg-rating" style="font-size:13px;font-weight:700;color:#F59E0B;"></div>
        </div>
        <div style="display:flex;gap:6px;margin-bottom:0;font-size:28px;">
          <span onclick="setSellerRating(1)" style="cursor:pointer;" class="seller-star">\u2606</span>
          <span onclick="setSellerRating(2)" style="cursor:pointer;" class="seller-star">\u2606</span>
          <span onclick="setSellerRating(3)" style="cursor:pointer;" class="seller-star">\u2606</span>
          <span onclick="setSellerRating(4)" style="cursor:pointer;" class="seller-star">\u2606</span>
          <span onclick="setSellerRating(5)" style="cursor:pointer;" class="seller-star">\u2606</span>
        </div>
        <button onclick="submitSellerRating()" style="width:100%;margin-top:10px;padding:10px;background:var(--dark);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Rating</button>
      </div>""",
"""      <!-- REVIEWS & RATINGS -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:14px;margin-bottom:12px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;letter-spacing:0.3px;">Reviews</div>
          <div id="bd-avg-rating" style="font-size:13px;font-weight:700;color:var(--earth);"></div>
        </div>
        <div id="bd-reviews-list"><div style="font-size:13px;color:var(--muted);text-align:center;padding:10px;">No reviews yet. Be the first!</div></div>
        <div style="margin-top:12px;border-top:1px solid var(--border);padding-top:12px;">
          <div style="font-size:12px;font-weight:600;color:var(--dark);margin-bottom:8px;">Write a Review</div>
          <div id="bd-star-rating" style="display:flex;gap:5px;margin-bottom:8px;font-size:20px;color:#ddd;">
            <span onclick="setReviewRating(1)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(2)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(3)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(4)" style="cursor:pointer;" class="star">\u2606</span>
            <span onclick="setReviewRating(5)" style="cursor:pointer;" class="star">\u2606</span>
          </div>
          <textarea id="bd-review-text" placeholder="Share your experience with this item..." style="width:100%;padding:10px;border:1.5px solid var(--border);border-radius:10px;font-size:13px;resize:none;height:70px;font-family:inherit;margin-bottom:8px;"></textarea>
          <input type="text" id="bd-reviewer-name" placeholder="Your name (optional)" style="margin-bottom:8px;font-size:13px;">
          <button onclick="submitReview()" style="width:100%;padding:10px;background:var(--earth);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Review</button>
        </div>
        <div style="margin-top:14px;border-top:1px solid var(--border);padding-top:12px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <div style="font-size:12px;font-weight:600;color:var(--dark);">Rate this Seller</div>
            <div id="bd-seller-avg-rating" style="font-size:12px;font-weight:700;color:var(--earth);"></div>
          </div>
          <div style="display:flex;gap:5px;margin-bottom:10px;font-size:20px;color:#ddd;">
            <span onclick="setSellerRating(1)" style="cursor:pointer;" class="seller-star">\u2606</span>
            <span onclick="setSellerRating(2)" style="cursor:pointer;" class="seller-star">\u2606</span>
            <span onclick="setSellerRating(3)" style="cursor:pointer;" class="seller-star">\u2606</span>
            <span onclick="setSellerRating(4)" style="cursor:pointer;" class="seller-star">\u2606</span>
            <span onclick="setSellerRating(5)" style="cursor:pointer;" class="seller-star">\u2606</span>
          </div>
          <button onclick="submitSellerRating()" style="width:100%;padding:10px;background:var(--earth);color:#fff;border:none;border-radius:10px;font-size:13px;font-weight:600;cursor:pointer;">Submit Rating</button>
        </div>
      </div>"""),

("""<a id="bd-wa-btn" href="#" target="_blank" style="flex:1.3;padding:13px;background:#25D366;color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">\U0001F4AC WhatsApp</a>
      <a id="bd-call-btn" href="#" style="flex:1;padding:13px;background:var(--dark);color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:5px;">\U0001F4DE Call</a>
      <button id="bd-dir-btn" style="width:46px;flex-shrink:0;padding:13px 0;background:#fff;border:1.5px solid var(--border);color:var(--dark);border-radius:11px;font-size:16px;cursor:pointer;">\U0001F4CD</button>""",
"""<a id="bd-wa-btn" href="#" target="_blank" style="flex:1.3;padding:13px;background:#25D366;color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:6px;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>WhatsApp</a>
      <a id="bd-call-btn" href="#" style="flex:1;padding:13px;background:var(--dark);color:#fff;border-radius:11px;font-size:13px;font-weight:700;text-decoration:none;text-align:center;display:flex;align-items:center;justify-content:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.362 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>Call</a>
      <button id="bd-dir-btn" style="width:46px;flex-shrink:0;padding:13px 0;background:#fff;border:1.5px solid var(--border);color:var(--dark);border-radius:11px;cursor:pointer;display:flex;align-items:center;justify-content:center;"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"/></svg></button>"""),

("if(item.stock){stockEl.style.display='block';stockEl.textContent='\U0001F4E6 '+item.stock+' units available';}",
 "if(item.stock){stockEl.style.display='flex';stockEl.style.alignItems='center';stockEl.innerHTML='<svg width=\"13\" height=\"13\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"margin-right:6px;flex-shrink:0;\"><path d=\"M21 8l-9-5-9 5 9 5 9-5z\"/><path d=\"M3 8v8l9 5 9-5V8\"/><path d=\"M12 13v8\"/></svg>'+item.stock+' units available';}"),

("""imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:64px;">\U0001F3EA</div>';""",
 """imgEl.innerHTML='<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#ddd" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l1-5h16l1 5"/><path d="M3 9a2 2 0 004 0 2 2 0 004 0 2 2 0 004 0 2 2 0 004 0"/><path d="M4 9v10h16V9"/><path d="M9 21v-6h6v6"/></svg></div>';"""),

("""  document.getElementById('bd-location').textContent = '\U0001F4CD '+item.location;
  var distEl = document.getElementById('bd-dist');
  if(buyerLat && buyerLng && item.latitude && item.longitude){
    var d = getDistance(buyerLat,buyerLng,item.latitude,item.longitude);
    distEl.textContent = '\U0001F4CD '+d+' km from you';
  } else { distEl.textContent = ''; }""",
"""  var pinIcon = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:-1px;margin-right:4px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 1118 0z"/><circle cx="12" cy="10" r="3"/></svg>';
  document.getElementById('bd-location').innerHTML = pinIcon+item.location;
  var distEl = document.getElementById('bd-dist');
  if(buyerLat && buyerLng && item.latitude && item.longitude){
    var d = getDistance(buyerLat,buyerLng,item.latitude,item.longitude);
    distEl.innerHTML = pinIcon+d+' km from you';
  } else { distEl.textContent = ''; }"""),

("      if(selResult.data.opening_hours) hoursEl.textContent='\U0001F550 '+selResult.data.opening_hours;",
 "      if(selResult.data.opening_hours) hoursEl.innerHTML='<svg width=\"11\" height=\"11\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" style=\"vertical-align:-1px;margin-right:4px;\"><circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 6v6l4 2\"/></svg>'+selResult.data.opening_hours;"),
]

count = 0
for i, (old, new) in enumerate(replacements, 1):
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        print("WARNING: pattern #" + str(i) + " not found, skipped")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. " + str(count) + "/" + str(len(replacements)) + " replacements applied.")
