"use client";

import React from "react";
import { DefaultPageLayout } from "@/subframe/layouts/DefaultPageLayout";
import * as SubframeCore from "@subframe/core";
import { IconButton } from "@/subframe/components/IconButton";
import { IconWithBackground } from "@/subframe/components/IconWithBackground";
import { Accordion } from "@/subframe/components/Accordion";
import { FilterChip } from "@/subframe/components/FilterChip";
import { Table } from "@/subframe/components/Table";

function RecipeDetailsPage() {
    return (
        <DefaultPageLayout>
            <div className="container max-w-none flex h-full w-full flex-col items-start gap-12 bg-default-background py-12 overflow-auto">
                <div className="flex w-full flex-wrap items-start gap-12">
                    <div className="flex min-w-[240px] grow shrink-0 basis-0 flex-col items-start gap-2 self-stretch">
                        <img
                            className="h-112 w-full flex-none rounded-md object-cover"
                            src="https://res.cloudinary.com/subframe/image/upload/v1718999371/uploads/302/g5jou2tvabjzl7exoihk.png"
                        />
                    </div>
                    <div className="flex min-w-[240px] grow shrink-0 basis-0 flex-col items-start justify-center gap-6 self-stretch">
                        <div className="flex w-full flex-col items-start justify-center gap-1">
                            <div className="flex w-full items-center justify-between">
                                <div className="flex items-center gap-2">
                  <span className="text-body-bold font-body-bold text-default-font">
                    Meals for Less
                  </span>
                                    <SubframeCore.Icon
                                        className="text-body font-body text-brand-700"
                                        name="FeatherCheckCircle"
                                    />
                                </div>
                                <IconButton
                                    icon="FeatherApple"
                                    onClick={(event: React.MouseEvent<HTMLButtonElement>) => {}}
                                />
                            </div>
                            <span className="text-heading-1 font-heading-1 text-default-font">
                Spicy Quinoa Salad
              </span>
                        </div>
                        <div className="flex w-full flex-col items-start gap-4 rounded-md border border-solid border-neutral-border bg-default-background px-4 py-4 shadow-sm">
                            <div className="flex w-full flex-col items-start gap-2">
                                <div className="flex w-full items-center gap-2">
                  <span className="line-clamp-1 grow shrink-0 basis-0 text-body-bold font-body-bold text-brand-700">
                    Total Savings
                  </span>
                                    <IconWithBackground icon="FeatherShoppingCart" />
                                </div>
                                <div className="flex items-end gap-2">
                  <span className="text-heading-2 font-heading-2 text-default-font">
                    $3
                  </span>
                                    <div className="flex items-end gap-2 pb-px">
                    <span className="text-body font-body text-subtext-color">
                      On Sale Items
                    </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <span className="text-caption-bold font-caption-bold text-subtext-color">
              Available at Food Lion
            </span>
                    </div>
                </div>
                <div className="flex w-full flex-col items-start gap-6">
                    <div className="flex w-full flex-col items-start gap-4 rounded-md border border-solid border-neutral-border bg-default-background shadow-sm">
                        <Accordion
                            trigger={
                                <div className="flex w-full items-center gap-2 px-6 py-6">
                  <span className="grow shrink-0 basis-0 text-heading-2 font-heading-2 text-default-font">
                    Recipe Information
                  </span>
                                    <Accordion.Chevron />
                                </div>
                            }
                            defaultOpen={true}
                        >
                            <div className="flex w-full grow shrink-0 basis-0 flex-col items-start gap-4 border-t border-solid border-neutral-border px-6 py-6">
                <span className="text-body font-body text-default-font">
                  This recipe for &#39;Spicy Quinoa Salad&#39; is a perfect
                  balance of flavors and nutrition. Loaded with protein-rich
                  quinoa, fresh vegetables, and a zesty dressing, it&#39;s a
                  delightful and healthy meal option. Ready to tantalize your
                  taste buds in just 20 minutes!
                </span>
                                <div className="flex flex-wrap items-center gap-6" />
                            </div>
                        </Accordion>
                    </div>
                    <div className="flex w-full flex-col items-start gap-4 rounded-md border border-solid border-neutral-border bg-default-background shadow-sm">
                        <Accordion
                            trigger={
                                <div className="flex w-full items-center gap-2 px-6 py-6">
                                    <div className="flex grow shrink-0 basis-0 items-center gap-4">
                    <span className="text-heading-2 font-heading-2 text-default-font">
                      Details
                    </span>
                                        <span className="text-body font-body text-subtext-color">
                      Popular Recipe
                    </span>
                                    </div>
                                    <Accordion.Chevron />
                                </div>
                            }
                            defaultOpen={true}
                        >
                            <div className="flex w-full grow shrink-0 basis-0 flex-col items-start gap-2 border-t border-solid border-neutral-border px-6 py-6">
                                <div className="flex w-full flex-wrap items-start gap-4 grid grid-cols-4 mobile:grid mobile:grid-cols-2">
                                    <div className="flex grow shrink-0 basis-0 flex-col items-start gap-2 rounded-md bg-neutral-50 px-4 py-4">
                    <span className="line-clamp-1 w-full text-caption-bold font-caption-bold text-subtext-color">
                      Pre-Sale Cost
                    </span>
                                        <span className="w-full text-heading-3 font-heading-3 text-default-font">
                      Salad
                    </span>
                                    </div>
                                    <div className="flex grow shrink-0 basis-0 flex-col items-start gap-2 rounded-md bg-neutral-50 px-4 py-4">
                    <span className="line-clamp-1 w-full text-caption-bold font-caption-bold text-subtext-color">
                      Savngs
                    </span>
                                        <span className="w-full text-heading-3 font-heading-3 text-default-font">
                      $4
                    </span>
                                    </div>
                                    <div className="flex grow shrink-0 basis-0 flex-col items-start gap-2 rounded-md bg-neutral-50 px-4 py-4">
                    <span className="line-clamp-1 w-full text-caption-bold font-caption-bold text-subtext-color">
                      Total
                    </span>
                                        <span className="w-full text-heading-3 font-heading-3 text-default-font">
                      $12
                    </span>
                                    </div>
                                </div>
                            </div>
                        </Accordion>
                    </div>
                    <div className="flex w-full flex-col items-start gap-4 rounded-md border border-solid border-neutral-border bg-default-background shadow-sm">
                        <Accordion
                            trigger={
                                <div className="flex w-full items-center gap-2 px-6 py-6">
                  <span className="text-heading-2 font-heading-2 text-default-font">
                    ingredients
                  </span>
                                </div>
                            }
                            defaultOpen={true}
                        >
                            <div className="flex w-full grow shrink-0 basis-0 flex-col items-start gap-4 border-t border-solid border-neutral-border px-6 py-6">
                                <div className="flex flex-wrap items-center gap-2">
                                    <FilterChip icon="FeatherThumbsUp">Best Value</FilterChip>
                                    <FilterChip icon="FeatherStar">Popular</FilterChip>
                                </div>
                                <Table
                                    header={
                                        <Table.HeaderRow>
                                            <Table.HeaderCell>Promotion</Table.HeaderCell>
                                            <Table.HeaderCell>Savings</Table.HeaderCell>
                                            <Table.HeaderCell>Store</Table.HeaderCell>
                                        </Table.HeaderRow>
                                    }
                                >
                                    <Table.Row>
                                        <Table.Cell>
                                            <div className="flex items-center gap-2">
                                                <SubframeCore.Icon
                                                    className="text-body font-body text-default-font"
                                                    name="FeatherTag"
                                                />
                                                <span className="whitespace-nowrap text-body-bold font-body-bold text-neutral-700">
                          Discount
                        </span>
                                            </div>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body-bold font-body-bold text-default-font">
                        $2 off
                      </span>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body font-body text-default-font">
                        Food Lion
                      </span>
                                        </Table.Cell>
                                    </Table.Row>
                                    <Table.Row>
                                        <Table.Cell>
                                            <div className="flex items-center gap-2">
                                                <SubframeCore.Icon
                                                    className="text-body font-body text-default-font"
                                                    name="FeatherThumbsUp"
                                                />
                                                <span className="whitespace-nowrap text-body-bold font-body-bold text-neutral-700">
                          Best Value
                        </span>
                                            </div>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body-bold font-body-bold text-default-font">
                        $10
                      </span>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body font-body text-default-font">
                        Food Lion
                      </span>
                                        </Table.Cell>
                                    </Table.Row>
                                    <Table.Row>
                                        <Table.Cell>
                                            <div className="flex items-center gap-2">
                                                <SubframeCore.Icon
                                                    className="text-body font-body text-default-font"
                                                    name="FeatherStar"
                                                />
                                                <span className="whitespace-nowrap text-body-bold font-body-bold text-neutral-700">
                          Top Pick
                        </span>
                                            </div>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body-bold font-body-bold text-default-font">
                        Top Rated
                      </span>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body font-body text-default-font">
                        Food Lion
                      </span>
                                        </Table.Cell>
                                    </Table.Row>
                                    <Table.Row>
                                        <Table.Cell>
                                            <div className="flex items-center gap-2">
                                                <SubframeCore.Icon
                                                    className="text-body font-body text-default-font"
                                                    name="FeatherTag"
                                                />
                                                <span className="whitespace-nowrap text-body-bold font-body-bold text-neutral-700">
                          Sale
                        </span>
                                            </div>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body-bold font-body-bold text-default-font">
                        $1.5 off
                      </span>
                                        </Table.Cell>
                                        <Table.Cell>
                      <span className="whitespace-nowrap text-body font-body text-default-font">
                        Food Lion
                      </span>
                                        </Table.Cell>
                                    </Table.Row>
                                </Table>
                            </div>
                        </Accordion>
                    </div>
                </div>
            </div>
        </DefaultPageLayout>
    );
}

export default RecipeDetailsPage;