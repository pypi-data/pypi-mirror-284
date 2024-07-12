from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import HttpUrl, field_validator

from rooms_shared_services.src.models.relations import CurrencyCode
from rooms_shared_services.src.models.texts.translations import TextTranslations
from rooms_shared_services.src.storage.models import UNSET, BaseDynamodbModel


class ProductDescription(BaseDynamodbModel):
    language_code: str
    full: str | None = None
    short: str | None = None
    translation_provider: str | None = None
    approved: bool | None = None


class ProductBrand(BaseDynamodbModel):
    id: UUID | None = None
    name: str | None = None
    website: HttpUrl | None = None
    catalog_pdf: HttpUrl | None = None
    description: str | None = None
    logo: HttpUrl | None = None


class ProductCollection(BaseDynamodbModel):
    id: UUID | None = None
    name: str | None = None
    catalog_pdf: HttpUrl | None = None
    description: str | None = None
    logo: HttpUrl | None = None


class ColorAttributes(BaseDynamodbModel):
    main_color: str | None = None
    main_color_image: HttpUrl | None = None
    color: str | None = None
    color_image: HttpUrl | None = None
    upholstery_color: str | None = None
    upholstery_color_image: HttpUrl | None = None
    front_color: str | None = None
    front_color_image: HttpUrl | None = None
    cabinet_color: str | None = None
    cabinet_color_image: HttpUrl | None = None


class ProductAttributes(BaseDynamodbModel):
    furniture_types: list[str]
    country_of_origin: list[str]
    materials: list[str]
    delivery_term: list[str]


class ImageSet(BaseDynamodbModel):
    small: HttpUrl | None = None
    medium: HttpUrl | None = None
    large: HttpUrl | None = None


class PackagePack(BaseDynamodbModel):
    ean: str | None = None
    weight: float | None = None
    length: float | None = None
    packNum: int | None = None  # noqa: N815
    height: float | None = None
    width: float | None = None


class StoreVariantRelatedValues(BaseDynamodbModel):
    default: str | int | datetime


class GeoRelatedValues(BaseDynamodbModel):
    default: StoreVariantRelatedValues
    israel: StoreVariantRelatedValues | None = None
    uk: StoreVariantRelatedValues | None = None


class LanguageRelatedValues(BaseDynamodbModel):
    default: GeoRelatedValues
    hebrew: GeoRelatedValues | None = None
    english: GeoRelatedValues | None = None
    russian: GeoRelatedValues | None = None


class RelatedValues(BaseDynamodbModel):
    wc: LanguageRelatedValues


class PriceValue(BaseDynamodbModel):
    currency: CurrencyCode | UNSET = "UNSET"
    value: float | UNSET = "UNSET"  # noqa: WPS110
    valid_untill: datetime | UNSET = "UNSET"

    @property
    def valid(self):
        return not (self.currency == "UNSET" or self.value == "UNSET")


class PriceValueCollection(BaseDynamodbModel):
    wc_israel_general_ils: PriceValue | None | UNSET = "UNSET"


class ProductSourceItem(BaseDynamodbModel):
    id: UUID | UNSET = "UNSET"
    product_group: str | UNSET = "UNSET"
    category: str | None | UNSET = "UNSET"
    room_category: str | None | UNSET = "UNSET"
    original_ident: str | None | UNSET = "UNSET"
    ident_code: str | None | UNSET = "UNSET"
    name: str | None | UNSET = "UNSET"
    slug: str | None | UNSET = "UNSET"
    created_at: datetime | None | UNSET = "UNSET"
    modified_at: datetime | None | UNSET = "UNSET"
    original_description_full: str | None | UNSET = "UNSET"
    original_description_short: str | None | UNSET = "UNSET"
    original_description_language_code: str | None | UNSET = "UNSET"
    origin_country: str | None | UNSET = "UNSET"
    pickup_location: str | None | UNSET = "UNSET"
    pickup_address: str | None | UNSET = "UNSET"
    shipment_term_code: str | None | UNSET = "UNSET"
    catalog_pdf: HttpUrl | None | UNSET = "UNSET"
    pickup_downtime: int | None | UNSET = "UNSET"
    brand_catalog_pages: list[int] | None | UNSET = "UNSET"
    collection_catalog_pages: list[int] | None | UNSET = "UNSET"
    brand_website_links: list[HttpUrl] | None | UNSET = "UNSET"
    sku: str | None | UNSET = "UNSET"
    wc_sku: str | None | UNSET = "UNSET"
    gross_weight: float | None | UNSET = "UNSET"
    net_weight: float | None | UNSET = "UNSET"
    height: float | None | UNSET = "UNSET"
    width: float | None | UNSET = "UNSET"
    depth: float | None | UNSET = "UNSET"
    related_ids: list[UUID] | None | UNSET = "UNSET"
    upsell_ids: list[UUID] | None | UNSET = "UNSET"
    cross_sell_ids: list[UUID] | None | UNSET = "UNSET"
    tags: list[str] | None | UNSET = "UNSET"
    image_sets: list[ImageSet] | None | UNSET = "UNSET"
    features: dict | None | UNSET = "UNSET"

    product_attributes: ProductAttributes | None | UNSET = "UNSET"
    color_attributes: ColorAttributes | None | UNSET = "UNSET"
    brand_name: str | None | UNSET = "UNSET"
    brand: ProductBrand | None | UNSET = "UNSET"
    collection: ProductCollection | None | UNSET = "UNSET"
    ean_GTIN: str | None | UNSET = "UNSET"  # noqa: N815
    qty_of_boxes: int | None | UNSET = "UNSET"
    brand_code: str | None | UNSET = "UNSET"
    volume_m3: float | None | UNSET = "UNSET"
    package_packs: list[PackagePack] | None | UNSET = "UNSET"
    qty_per_box: int | None | UNSET = "UNSET"
    ean: str | None | UNSET = "UNSET"
    withdrawn: bool | None | UNSET = "UNSET"
    pcn: str | None | UNSET = "UNSET"
    categories_raw: list[str] | None | UNSET = "UNSET"
    wc_categories: list[str] | None | UNSET = "UNSET"
    published: RelatedValues | None | UNSET = "UNSET"
    name_translations: TextTranslations | None | UNSET = "UNSET"
    full_description_translations: TextTranslations | None | UNSET = "UNSET"
    short_description_translations: TextTranslations | None | UNSET = "UNSET"
    price_value_collection: PriceValueCollection | None | UNSET = "UNSET"
    price_base: PriceValue | None | UNSET = "UNSET"

    furniture_types: list[str] | None | UNSET = "UNSET"
    country_of_origin: list[str] | None | UNSET = "UNSET"
    materials: list[str] | None | UNSET = "UNSET"
    delivery_term: list[str] | None | UNSET = "UNSET"

    @field_validator(
        "brand_catalog_pages",
        "collection_catalog_pages",
        "brand_website_links",
        "related_ids",
        "upsell_ids",
        "cross_sell_ids",
        "tags",
        "image_sets",
        "package_packs",
        "categories_raw",
        mode="before",
    )
    @classmethod
    def skip_invalid_lists(cls, item_value: Any) -> str:
        if not isinstance(item_value, list) and item_value is not None:
            return "UNSET"
        return item_value
