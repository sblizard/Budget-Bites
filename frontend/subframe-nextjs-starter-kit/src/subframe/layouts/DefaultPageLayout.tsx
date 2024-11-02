"use client";
/*
 * Documentation:
 * Default Page Layout — https://app.subframe.com/3ea4d9617b64/library?component=Default+Page+Layout_a57b1c43-310a-493f-b807-8cc88e2452cf
 * Topbar with center search — https://app.subframe.com/3ea4d9617b64/library?component=Topbar+with+center+search_3bd79561-0143-4651-931b-3b7260b0b798
 */

import React from "react";
import * as SubframeCore from "@subframe/core";
import { TopbarWithCenterSearch } from "../components/TopbarWithCenterSearch";

interface DefaultPageLayoutRootProps
  extends React.HTMLAttributes<HTMLDivElement> {
  children?: React.ReactNode;
  className?: string;
}

const DefaultPageLayoutRoot = React.forwardRef<
  HTMLElement,
  DefaultPageLayoutRootProps
>(function DefaultPageLayoutRoot(
  { children, className, ...otherProps }: DefaultPageLayoutRootProps,
  ref
) {
  return (
    <div
      className={SubframeCore.twClassNames(
        "flex h-screen w-full flex-col items-center",
        className
      )}
      ref={ref as any}
      {...otherProps}
    >
      <TopbarWithCenterSearch
        leftSlot={
          <>
            <img
              className="h-11 flex-none object-cover"
              src="https://res.cloudinary.com/subframe/image/upload/v1730582667/uploads/4443/ermo4qtfrqpmepdo3wnq.png"
            />
            <div className="flex items-center gap-2">
              <TopbarWithCenterSearch.NavItem selected={true}>
                Home
              </TopbarWithCenterSearch.NavItem>
            </div>
          </>
        }
      />
      {children ? (
        <div className="flex w-full grow shrink-0 basis-0 flex-col items-start gap-4 overflow-y-auto bg-default-background">
          {children}
        </div>
      ) : null}
    </div>
  );
});

export const DefaultPageLayout = DefaultPageLayoutRoot;
