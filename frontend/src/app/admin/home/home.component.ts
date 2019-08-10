import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  navigation = [
    { link: '/home/product', label: 'Quản lý sảm phẩm', icon: "fa fa-tasks", id: "manage_product" },
    { link: '/home/category', label: 'Quản lý loại sản phẩm', icon: "fas fa-i-cursor", id: "manage_category" },
    { link: '/home/staff', label: 'Quản lý nhân viên', icon: "fas fa-pastafarianism", id: "manage_staff" },
  ];
  navigationSideMenu = [...this.navigation];
  constructor() { }

  ngOnInit() {
  }

}
