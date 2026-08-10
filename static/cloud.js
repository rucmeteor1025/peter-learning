// ===== 云端同步（Supabase）=====
// 学习进度 / 错题本 / 学习币 / 游戏锁定，跨设备同步
const SUPABASE_URL = 'https://luyfkjzmysbefruckovp.supabase.co';
const SUPABASE_KEY = 'sb_publishable_R6Ql3piTnM7XsUnbPTGRKA_vN6qoBO4';

// 拉取某用户云端数据，返回 { username, data, updated_at } 或 null
async function cloudLoad(username) {
	try {
	const res = await fetch(SUPABASE_URL + '/rest/v1/user_data?username=eq.' + encodeURIComponent(username) + '&select=*', {
	headers: { 'apikey': SUPABASE_KEY, 'Authorization': 'Bearer ' + SUPABASE_KEY }
	});
	if (!res.ok) return null;
	const rows = await res.json();
	if (!rows || !rows.length) return null;
	return rows[0];
	} catch(e) { return null; }
}

// 推送用户数据到云端（upsert）
async function cloudSave(username, data) {
	try {
	const body = { username: username, data: data, updated_at: new Date().toISOString() };
	const res = await fetch(SUPABASE_URL + '/rest/v1/user_data?on_conflict=username', {
	method: 'POST',
	headers: {
	'apikey': SUPABASE_KEY,
	'Authorization': 'Bearer ' + SUPABASE_KEY,
	'Content-Type': 'application/json',
	'Prefer': 'resolution=merge-duplicates'
	},
	body: JSON.stringify(body)
	});
	return res.ok;
	} catch(e) { return false; }
}

// ===== 本地数据打包 / 合并 =====
function localBundle(username) {
	const k = (x) => 'peter_d_' + username + '_' + x;
	try {
	return {
	progress: JSON.parse(localStorage.getItem(k('progress')) || '{}'),
	wrong: JSON.parse(localStorage.getItem(k('wrong')) || '{}'),
	coins: parseInt(localStorage.getItem(k('coins')) || '0') || 0,
	gameEnd: parseInt(localStorage.getItem(k('gameEnd')) || '0') || 0
	};
	} catch(e) { return { progress: {}, wrong: {}, coins: 0, gameEnd: 0 }; }
}
function applyBundle(username, bundle) {
	if (!bundle) return;
	const k = (x) => 'peter_d_' + username + '_' + x;
	if (bundle.progress && typeof bundle.progress === 'object') localStorage.setItem(k('progress'), JSON.stringify(bundle.progress));
	if (bundle.wrong && typeof bundle.wrong === 'object') localStorage.setItem(k('wrong'), JSON.stringify(bundle.wrong));
	if (typeof bundle.coins === 'number') localStorage.setItem(k('coins'), String(bundle.coins));
	if (typeof bundle.gameEnd === 'number') localStorage.setItem(k('gameEnd'), String(bundle.gameEnd));
}
function localSyncTs(username) { try { return parseInt(localStorage.getItem('peter_d_' + username + '_sync_ts') || '0') || 0; } catch(e) { return 0; } }
function touchSyncTs(username) { try { localStorage.setItem('peter_d_' + username + '_sync_ts', String(Date.now())); } catch(e) {} }

// ===== 登录时同步（拉取云端合并 / 推送本地）=====
async function syncFromCloud(username) {
	const row = await cloudLoad(username);
	const hasLocal = localStorage.getItem('peter_d_' + username + '_progress') !== null;
	const localTs = localSyncTs(username);
	const cloudTs = row ? new Date(row.updated_at).getTime() : 0;
	if (row && (!hasLocal || cloudTs > localTs)) {
	// 云端更新 → 拉到本地
	applyBundle(username, row.data);
	touchSyncTs(username);
	return 'pulled';
	}
	if (!row && hasLocal) {
	// 只有本地 → 推到云端
	const ok = await cloudSave(username, localBundle(username));
	if (ok) touchSyncTs(username);
	return 'pushed';
	}
	if (row && hasLocal && localTs >= cloudTs) {
	// 本地更新 → 推到云端
	const ok = await cloudSave(username, localBundle(username));
	if (ok) touchSyncTs(username);
	return 'pushed';
	}
	return 'none';
}

// ===== 保存后防抖推送（本地改动自动同步到云端）=====
let cloudTimer = null;
function scheduleCloudPush() {
	if (typeof USERNAME === 'undefined' || !USERNAME) return;
	clearTimeout(cloudTimer);
	cloudTimer = setTimeout(() => {
	cloudSave(USERNAME, localBundle(USERNAME)).then(ok => { if (ok) touchSyncTs(USERNAME); });
	}, 2000);
}
