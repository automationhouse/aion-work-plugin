# AION WORK

AION WORK brings daily work routines, MarketingOS, SalesOS, CustomerOS, personal MIND access and team collaboration to Codex and Claude Code. The plugin connects to AION over MCP. Its skills and working methods are primarily in Polish.

This is AION's distribution repository. Installing the plugin is separate from connecting an AION account. Protected features require an eligible AION account; individual modules and resources have their own access rules. Installing this public package does not grant access to paid methods, company data or private MIND content.

## Install

Use a current version of Codex or Claude Code with plugin marketplace support. Git is required to download this marketplace. Run the commands for your client in a terminal.

### Claude Code

```sh
claude plugin marketplace add automationhouse/aion-work-plugin --scope user
claude plugin install aion-work@aion-prod --scope user
```

### Codex

```sh
codex plugin marketplace add automationhouse/aion-work-plugin
codex plugin add aion-work@aion-prod
```

You can also select AION WORK from the `aion-prod` source in Codex's plugin browser after adding the marketplace.

Start a new session after installation. Invoke the `aion-work:start` skill (in Claude Code: `/aion-work:start`) and complete the client's AION sign-in and consent flow. The server is `https://app.aionwork.com/api/mcp/work`. Never paste passwords, tokens or OAuth callback URLs into a chat or repository.

The first successful check reads your profile and AION's core working instructions. An installed plugin alone does not confirm account access. Git and Python 3.10+ are needed for the optional repository guard and folder health workflows, not for accessing remote methods alone. GitHub repository access is authorized separately from AION sign-in.

## Update

### Claude Code

```sh
claude plugin update aion-work@aion-prod
```

Use the same installation scope if you originally chose a scope other than `user`. Automatic updates for custom marketplaces are off by default; enable them for `aion-prod` in the plugin marketplace settings if desired.

### Codex

```sh
codex plugin marketplace upgrade aion-prod
```

Refresh the installed AION WORK plugin using your client's plugin controls. If your version has no update action, remove and add only this plugin:

```sh
codex plugin remove aion-work@aion-prod
codex plugin add aion-work@aion-prod
```

Start a new session and verify the plugin version, AION tools, profile and core instructions. Reconnect through the native sign-in flow if requested. Do not copy credentials or replace your entire client configuration.

## Move from a downloaded ZIP

If `aion-prod` already points to a local ZIP extraction, replace that marketplace registration with this GitHub source. Do not register a second AION MCP server. Note your existing source path and installation scope first, and keep the old extraction until the new installation works.

Claude Code:

```sh
claude plugin uninstall aion-work@aion-prod --scope user
claude plugin marketplace remove aion-prod
claude plugin marketplace add automationhouse/aion-work-plugin --scope user
claude plugin install aion-work@aion-prod --scope user
```

Codex:

```sh
codex plugin remove aion-work@aion-prod
codex plugin marketplace remove aion-prod
codex plugin marketplace add automationhouse/aion-work-plugin
codex plugin add aion-work@aion-prod
```

These commands replace only the AION WORK installation and its marketplace registration. Keep your work folders, other plugins and client permissions. Complete native sign-in again if the client requests it, then verify access in a fresh session without repeating setup for an existing work folder.

## Privacy and package contents

The package contains skills, runtime references, local guard/health scripts and public OAuth client settings. It contains no account credentials, customer data or copies of protected AION methods. Private profiles and journals belong outside company repositories and shared folders. The optional guard checks files before publication; installation does not install Git hooks or run the guard.

The marketplace name is `aion-prod`, and the plugin ID is `aion-work`. Both remain stable across releases. `build-info.json` at the repository root records the released version and MCP endpoint. Native Codex and Claude manifests use separate OAuth client configurations.

## Help and releases

Use [AION WORK](https://app.aionwork.com/work-plugin) for product access and account management. Report reproducible installation problems through [GitHub Issues](https://github.com/automationhouse/aion-work-plugin/issues), including the client and plugin versions. Do not include private work content, credentials or OAuth URLs.

This repository contains generated releases. Plugin changes are maintained in the AION source repository and published here after review. Changes to bundled skills require a versioned plugin update; authorized remote methods can be updated separately. Public availability of the installation package does not grant additional rights to the AION service or its protected content.
