import { Component, OnInit, Output, Input } from '@angular/core';

@Component({
  selector: 'app-aside-menu',
  templateUrl: './aside-menu.component.html',
  styleUrls: ['./aside-menu.component.css']
})
export class AsideMenuComponent implements OnInit {
  @Input() asideMenu : [];
  constructor() { }

  ngOnInit() {
    console.log(this.asideMenu);
    
  }

}
