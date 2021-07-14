import { Injectable } from "@angular/core";
import { Player } from "./player";

@Injectable({
    providedIn: 'root',
  })
  export class AppStateService {
      selectedPlayer?: Player;

      constructor() {
        console.info('app-state constructor')
      }
  }
