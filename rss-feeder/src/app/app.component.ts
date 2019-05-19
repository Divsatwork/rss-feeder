import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FeedService } from '../app/feed.service';
import { FeedItem } from './feeditem.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  showForm: boolean;
  showDesc: boolean;
  showError: boolean;
  loading: boolean;
  feed: FeedItem[] = [];
  constructor(private http: HttpClient,
              private feedService: FeedService) {
    this.showForm = true;
    this.showDesc = true;
    this.loading = false;
    this.showError = false;
  }

  onSubmit(value: string): void {
    this.showForm = false;
    this.loading = true;
    const source = this.feedService.getData(value['url']);
    source.subscribe((res: FeedItem[]) => {
      this.showDesc = false;
      if (res.length !== undefined) {
        this.feed = res;
        this.loading = false;
      } else {
        this.loading = false;
        this.showError = true;
      }
    }, err => {
      console.log('Error while fetching data from server!');
      this.showError = true;
    });
  }
}
