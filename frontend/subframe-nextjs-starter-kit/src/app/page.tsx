"use client";

import React from "react";
import { ListingCard } from "@/subframe/components/ListingCard";
import { Button } from "@/subframe/components/Button";

function MarketplaceListingsHome() {
    return (
        <div className="flex h-full w-full flex-col items-start gap-2">
            <div className="container max-w-none flex w-full grow shrink-0 basis-0 flex-col items-start gap-4 bg-default-background py-12 mobile:flex-col mobile:gap-3 mobile:rounded-md mobile:border mobile:border-solid mobile:border-neutral-border mobile:bg-default-background mobile:px-6 mobile:py-12 mobile:shadow-sm">
                <div className="flex h-px w-full flex-none flex-col items-center gap-2 bg-neutral-border" />
                <div className="flex w-full flex-col items-start gap-6">
                    <div className="flex w-full flex-wrap items-start gap-6 grid grid-cols-3 mobile:grid mobile:grid-cols-1">
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Spicy Chickpea Salad"
                            rating="4.9"
                            desc="Quick and easy to prepare"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$5.20"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Garlic Butter Pasta"
                            rating="4.7"
                            desc="Rich and savory taste"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$7.50"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Black Bean Tacos"
                            rating="4.8"
                            desc="Packed with protein"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$6.00"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Cucumber Mint Salad"
                            rating="4.6"
                            desc="Refreshing and light"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$4.85"
                            unit="per serving"
                            showBadge={true}
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Pumpkin Soup"
                            rating="4.8"
                            desc="Perfect for chilly days"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$5.75"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Lemon Herb Chicken"
                            rating="4.9"
                            desc="Zesty and filling"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$6.40"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Mushroom Risotto"
                            rating="4.7"
                            desc="Comforting classic"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$5.00"
                            unit="per serving"
                        />
                        <ListingCard
                            image="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                            title="Parmesan Zucchini Fries"
                            rating="4.8"
                            desc="Crispy and delicious"
                            dates="Sale: Oct 10 – Oct 17"
                            price="$4.50"
                            unit="per serving"
                            showBadge={true}
                        />
                    </div>
                </div>
                <div className="flex h-px w-full flex-none flex-col items-center gap-2 bg-neutral-border" />
                <div className="flex w-full flex-col items-center justify-center gap-4 px-12 py-12">
          <span className="text-heading-3 font-heading-3 text-default-font">
            Eat better, spend less.
          </span>
                    <Button
                        variant="brand-secondary"
                        onClick={(event: React.MouseEvent<HTMLButtonElement>) => {}}
                    >
                        Contact Us
                    </Button>
                </div>
            </div>
        </div>
    );
}

export default MarketplaceListingsHome;