# Installing Blightfall — walkthrough and troubleshooting

## 1. Install Prism Launcher

Get it from https://prismlauncher.org/download/ (Windows, macOS or Linux). You don't need
to install Java yourself: Prism downloads Java 8 the first time you launch.

## 2. Get whitelisted

Send Adam your **exact** Minecraft Java username (capitals matter). Until he adds you,
joining fails with "You are not white-listed on this server".

## 3. Import the pack

- Prism → **Add Instance** (top left) → **Import**.
- Paste the release link from the README into the box, or click **Browse** and pick the
  `Blightfall-Server-x.y.z.zip` you downloaded from the Releases page.
- Click **OK**. It's about 120 MB.

## 4. Play

- Select **Blightfall (server)** and click **Launch**.
- **Multiplayer** → **Blightfall** → **Join Server**.
- The first launch takes a few minutes (it's a big 1.7.10 pack). That's normal.

## Troubleshooting

**"Blightfall is starting — rejoin in 2 minutes"** — the server sleeps after 15 minutes
with nobody online and your join just woke it up. Wait a couple of minutes and join again.

**"You are not white-listed on this server"** — Adam hasn't added your exact username yet.

**Prism asks about Java / the game won't start** — right-click the instance → **Edit** →
**Settings** → **Java** → tick **Auto-detect / download Java** (it must be Java 8, not
17 or 21). Minecraft 1.7.10 does not run on newer Java.

**Out of memory / very slow** — the instance asks for 6 GB. On an 8 GB PC lower it to 4 GB
(Edit → Settings → Java → Maximum memory). On 16 GB+ you can leave it.

**Mods don't match the server ("Mod rejections" on join)** — delete the instance and
re-import the latest release zip. Don't add or update mods yourself.

**macOS** — 1.7.10 runs, but on Apple Silicon it's slow; that's the game's age, not the pack.

**Can't connect / times out** — the server might be down for maintenance, or the address
changed. Ask in the group chat.
