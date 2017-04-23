declare module "rc-upload" {
    import * as React from 'react';

    export interface UploadComponentProps {
        component?: string;
        prefixCls?: string;
        action: string;
        name?: string;
        multipart?: boolean;
        onError?: (err: any, ret: any, file: any) => void;
        onSuccess?: (ret: any, file: any) => void;
        onProgress: (e: any, file: any) => void;
        onStart?: (file: any) => void;
        data?: any;
        headers?: { [propName: string]: string };
        accept: string;
        multiple?: boolean;
        disabled: boolean;
        beforeUpload?: (file: any, fileList: any) => void;
        customRequest?: () => void;
        onReady?: () => void;
        withCredentials?: boolean;
        supportServerRender?: boolean;

    }

    class Upload extends React.Component<UploadComponentProps, undefined> {
        
    }


}