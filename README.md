# EDH Sim

A Commander / EDH simulator focused on fast goldfishing, AI opponents, and a polished card-game UI.

## Goals
- Goldfish Commander decks quickly
- Simulate 1v1 first, then expand toward multiplayer Commander
- Computer-controlled opponents
- Track zones, life, commander tax, mana, combat, triggers, and turn state
- Import decklists
- Separate rules/game state from presentation
- Build toward a polished MTG Arena / Hearthstone-inspired interface

## Project status
This repository is the new home of the Commander simulator project previously referred to as Commander Sim.

The earlier local prototype/Forge archive is not committed here yet because the original uploaded ZIP source is not currently recoverable from the project file library. This repo starts with a clean architecture so recovered or rebuilt pieces can be integrated safely.

## Planned architecture
- `src/engine/` — game state, turns, zones, actions
- `src/ai/` — computer opponent policies
- `src/cards/` — card/deck models and import
- `src/ui/` — presentation layer
- `tests/` — engine tests
- `docs/` — design notes and roadmap

## Near-term roadmap
1. Decklist parser
2. Core player / card / zone models
3. Draw, play land, mana, cast, pass-turn loop
4. Goldfish runner
5. Commander zone + commander tax
6. Combat
7. Simple opponent AI
8. Browser UI
9. Multiplayer state
10. Rules/stack expansion
