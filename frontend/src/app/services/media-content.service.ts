import { Injectable } from '@angular/core';

import { s3MediaResource,
    MAJOR_ROLE_TOOL_LIST, MAJOR_ROLE_EDUCATIONS,
    PORTFOLIO_COVER_IMAGES,
    HIGHLIGHT_COVER_IMAGES,
    THEMED_ACTIONS
} from "./media.mock-data";

@Injectable({
    providedIn: 'root'
})
export class MediaContentService {

    constructor(
    ) { }

    get majorRolesToolList(): s3MediaResource[] {
        return MAJOR_ROLE_TOOL_LIST;
    }

    get majorRolesEducations(): any[] {
        return MAJOR_ROLE_EDUCATIONS;
    }

    get portfolioCoverImages(): any {
        return PORTFOLIO_COVER_IMAGES;
    }

    get highlightCoverImages(): any {
        return HIGHLIGHT_COVER_IMAGES;
    }

    /* * *

        Actions and Navigations

    * * */

    get navActions() {
        return this.getContentListByKeys(['portfolio', 'blog', 'profile']);
    }

    get homeHeadlineActions() {
        return this.getContentListByKeys(['portfolio', 'profile']);
    }

    get homeBottomThemedActions(): any {
        return this.getContentListByKeys(['blog', 'portfolio', 'design']);
    }

    public getContentListByKeys(keys) {
        let contentList = [];
        for (let k of keys) {
            contentList.push(THEMED_ACTIONS[k]);
        }
        return contentList;
    }
}
