"use client";
/*
 * Documentation:
 * Listing Card — https://app.subframe.com/3ea4d9617b64/library?component=Listing+Card_d6c7c6a0-4f41-4d49-aeeb-17baed4bc7ad
 * Badge — https://app.subframe.com/3ea4d9617b64/library?component=Badge_97bdb082-1124-4dd7-a335-b14b822d0157
 * Icon Button — https://app.subframe.com/3ea4d9617b64/library?component=Icon+Button_af9405b1-8c54-4e01-9786-5aad308224f6
 */

import React from "react";
import * as SubframeCore from "@subframe/core";
import { Badge } from "./Badge";
import { IconButton } from "./IconButton";

interface ListingCardRootProps
  extends Omit<React.HTMLAttributes<HTMLDivElement>, "title"> {
  image?: string;
  title?: React.ReactNode;
  rating?: React.ReactNode;
  desc?: React.ReactNode;
  dates?: React.ReactNode;
  price?: React.ReactNode;
  unit?: React.ReactNode;
  showBadge?: boolean;
  className?: string;
}

const ListingCardRoot = React.forwardRef<HTMLElement, ListingCardRootProps>(
  function ListingCardRoot(
    {
      image,
      title,
      rating,
      desc,
      dates,
      price,
      unit,
      showBadge = false,
      className,
      ...otherProps
    }: ListingCardRootProps,
    ref
  ) {
    return (
      <div
        className={SubframeCore.twClassNames(
          "group/d6c7c6a0 flex w-full min-w-[240px] max-w-[384px] cursor-pointer flex-col items-start gap-2 overflow-hidden pb-2 h-auto",
          className
        )}
        ref={ref as any}
        {...otherProps}
      >
        <div
          className={SubframeCore.twClassNames(
            "flex w-full flex-col items-start justify-center overflow-hidden rounded-md relative",
            { "h-auto w-full flex-none": showBadge }
          )}
        >
          <Badge
            className={SubframeCore.twClassNames(
              "hidden absolute top-4 left-2",
              { flex: showBadge }
            )}
            variant="neutral"
          >
            Guest favorite
          </Badge>
          <IconButton
            className={SubframeCore.twClassNames("absolute top-2 right-2", {
              "absolute top-2 right-2": showBadge,
            })}
            variant="inverse"
            icon="FeatherHeart"
          />
          <IconButton
            className="hidden absolute right-2 group-hover/d6c7c6a0:flex"
            variant="inverse"
            size="medium"
            icon="FeatherChevronRight"
          />
          <IconButton
            className={SubframeCore.twClassNames(
              "hidden absolute right-2 group-hover/d6c7c6a0:flex group-hover/d6c7c6a0:absolute group-hover/d6c7c6a0:left-2",
              { "absolute left-2": showBadge }
            )}
            variant="inverse"
            size="medium"
            icon="FeatherChevronLeft"
          />
          {image ? (
            <img className="h-60 w-full flex-none object-cover" src={image} />
          ) : null}
        </div>
        <div className="flex w-full flex-col items-start gap-1">
          <div className="flex w-full items-center gap-2">
            {title ? (
              <span className="grow shrink-0 basis-0 text-body-bold font-body-bold text-default-font">
                {title}
              </span>
            ) : null}
            <div className="flex items-center gap-1">
              <SubframeCore.Icon
                className="text-caption-bold font-caption-bold text-default-font"
                name="FeatherStar"
              />
              {rating ? (
                <span className="text-caption-bold font-caption-bold text-default-font">
                  {rating}
                </span>
              ) : null}
            </div>
          </div>
          {desc ? (
            <span className="line-clamp-2 w-full text-caption font-caption text-subtext-color">
              {desc}
            </span>
          ) : null}
          {dates ? (
            <span className="line-clamp-2 w-full text-caption font-caption text-subtext-color">
              {dates}
            </span>
          ) : null}
        </div>
        <div className="flex items-center gap-1">
          {price ? (
            <span className="line-clamp-2 text-body-bold font-body-bold text-default-font">
              {price}
            </span>
          ) : null}
          {unit ? (
            <span className="line-clamp-2 text-body-bold font-body-bold text-default-font">
              {unit}
            </span>
          ) : null}
        </div>
      </div>
    );
  }
);

export const ListingCard = ListingCardRoot;
